"""
tools.py — All tool implementations for the Job Seeker Agent
Tools NEVER raise exceptions — always return strings or dicts.
"""

import re
from datetime import datetime
from typing import Optional


# TOOL 1: CTC → In-Hand Salary Calculator
# Non-trivial tool: applies real PF, PT, TDS deduction logic

PROFESSIONAL_TAX_BY_STATE = {
    "maharashtra": 2500,
    "karnataka": 2400,
    "west bengal": 2400,
    "telangana": 2400,
    "andhra pradesh": 2400,
    "tamil nadu": 2496,
    "gujarat": 2400,
    "kerala": 1200,
    "madhya pradesh": 1800,
}

NO_PT_STATES = [
    "delhi", "haryana", "rajasthan", "uttar pradesh", "up",
    "himachal pradesh", "uttarakhand", "bihar", "jharkhand",
    "goa", "punjab"
]


def calculate_inhand_salary(
    ctc_annual: float,
    variable_percent: float = 0.0,
    state: str = "karnataka",
    tax_regime: str = "new",
    has_hra_exemption: bool = True,
    rent_paid_monthly: float = 0.0,
    is_metro: bool = True
) -> dict:
    """
    Calculate monthly in-hand salary from annual CTC.
    Returns a detailed breakdown dict, never raises exceptions.
    """
    try:
        ctc_annual = float(ctc_annual)
        if ctc_annual <= 0:
            return {"error": "CTC must be a positive number."}
        if ctc_annual > 10_00_00_000:  # sanity check > 10 Cr
            return {"error": "Please enter CTC in rupees, not lakhs. E.g. 600000 for 6 LPA."}

Salary structure breakdown ──────────────────────────────────────
        variable_fraction = min(variable_percent / 100.0, 0.40)  # cap at 40%
        fixed_ctc = ctc_annual * (1 - variable_fraction)

        # Employer PF and Gratuity are part of CTC — subtract to get gross salary
        basic = fixed_ctc * 0.40
        employer_pf = basic * 0.12
        gratuity_annual = basic * (15 / 26) * (1 / 12) * 12  # simplified annual
        gross_salary = fixed_ctc - employer_pf - min(gratuity_annual, fixed_ctc * 0.05)

Monthly components ──────────────────────────────────────────────
        basic_monthly = basic / 12
        hra_monthly = basic_monthly * (0.50 if is_metro else 0.40)
        special_allowance_monthly = (gross_salary / 12) - basic_monthly - hra_monthly
        special_allowance_monthly = max(special_allowance_monthly, 0)
        gross_monthly = gross_salary / 12

Deductions ─────────────────────────────────────────────────────
        # 1. Employee PF (12% of basic)
        employee_pf_monthly = basic_monthly * 0.12

        # 2. Professional Tax
        state_lower = state.strip().lower()
        if state_lower in NO_PT_STATES:
            pt_annual = 0
        else:
            pt_annual = PROFESSIONAL_TAX_BY_STATE.get(state_lower, 2400)
        pt_monthly = pt_annual / 12

        # 3. TDS estimation
        taxable_income = _estimate_taxable_income(
            gross_salary=gross_salary,
            basic=basic,
            hra_annual=hra_monthly * 12,
            tax_regime=tax_regime,
            has_hra_exemption=has_hra_exemption,
            rent_paid_monthly=rent_paid_monthly,
            is_metro=is_metro,
            employee_pf_annual=employee_pf_monthly * 12,
            pt_annual=pt_annual,
        )
        annual_tax = _compute_tax(taxable_income, tax_regime)
        tds_monthly = max(annual_tax / 12, 0)

Final in-hand ───────────────────────────────────────────────────
        total_deductions_monthly = employee_pf_monthly + pt_monthly + tds_monthly
        inhand_monthly = gross_monthly - total_deductions_monthly

        return {
            "ctc_annual": round(ctc_annual),
            "fixed_ctc_annual": round(fixed_ctc),
            "variable_ctc_annual": round(ctc_annual * variable_fraction),
            "gross_monthly": round(gross_monthly),
            "basic_monthly": round(basic_monthly),
            "hra_monthly": round(hra_monthly),
            "special_allowance_monthly": round(special_allowance_monthly),
            "deductions": {
                "employee_pf_monthly": round(employee_pf_monthly),
                "professional_tax_monthly": round(pt_monthly),
                "tds_monthly": round(tds_monthly),
                "total_deductions_monthly": round(total_deductions_monthly),
            },
            "inhand_monthly": round(inhand_monthly),
            "inhand_annual": round(inhand_monthly * 12),
            "effective_tax_rate_percent": round((annual_tax / gross_salary * 100), 2) if gross_salary > 0 else 0,
            "tax_regime": tax_regime,
            "state": state,
            "employer_pf_monthly": round(employer_pf / 12),
            "note": f"Variable pay of ₹{round(ctc_annual * variable_fraction):,}/year is excluded from monthly calculation."
                    if variable_fraction > 0 else "",
        }

    except (ValueError, TypeError) as e:
        return {"error": f"Could not process input: {str(e)}. Please provide CTC as a number in rupees."}
    except Exception as e:
        return {"error": f"Calculation failed: {str(e)}"}


def _estimate_taxable_income(
    gross_salary, basic, hra_annual, tax_regime, has_hra_exemption,
    rent_paid_monthly, is_metro, employee_pf_annual, pt_annual
) -> float:
    if tax_regime == "new":
        # New regime: standard deduction ₹75,000 only
        return max(gross_salary - 75000, 0)
    else:
        # Old regime
        deductions = 0
        # Standard deduction
        deductions += 50000
        # HRA exemption (if renting)
        if has_hra_exemption and rent_paid_monthly > 0:
            rent_annual = rent_paid_monthly * 12
            hra_exempt = min(
                hra_annual,
                rent_annual - 0.10 * basic,
                (0.50 if is_metro else 0.40) * basic
            )
            deductions += max(hra_exempt, 0)
        # 80C: PF + assume ELSS/insurance up to 1.5L limit
        deductions += min(employee_pf_annual + 50000, 150000)
        # Professional Tax
        deductions += pt_annual
        return max(gross_salary - deductions, 0)


def _compute_tax(taxable_income: float, regime: str) -> float:
    if regime == "new":
        # New regime slabs (FY2024-25)
        # Rebate u/s 87A: if taxable income ≤ ₹7,00,000 → tax liability = 0 (full rebate)
        if taxable_income <= 300000:
            tax = 0.0
        elif taxable_income <= 700000:
            # Slab rate would be 5% on (income - 3L), but Section 87A rebate
            # cancels the entire tax for income ≤ ₹7L under new regime.
            tax = 0.0
        elif taxable_income <= 1000000:
            # 3-7L: ₹20,000 tax; 7L-10L: 10%
            tax = 20000 + (taxable_income - 700000) * 0.10
        elif taxable_income <= 1200000:
            # base at 10L = 20000 + 30000 = 50000; 10-12L: 15%
            tax = 50000 + (taxable_income - 1000000) * 0.15
        elif taxable_income <= 1500000:
            # base at 12L = 50000 + 30000 = 80000; 12-15L: 20%
            tax = 80000 + (taxable_income - 1200000) * 0.20
        else:
            # base at 15L = 80000 + 60000 = 140000; >15L: 30%
            tax = 140000 + (taxable_income - 1500000) * 0.30
        # Health & Education Cess 4%
        return tax * 1.04
    else:
        # Old regime slabs (FY2024-25)
        if taxable_income <= 250000:
            tax = 0.0
        elif taxable_income <= 500000:
            # Slab rate would be 5% on (income - 2.5L), but Section 87A rebate
            # cancels the entire tax for income ≤ ₹5L under old regime.
            tax = 0.0
        elif taxable_income <= 1000000:
            tax = 12500 + (taxable_income - 500000) * 0.20
        else:
            tax = 112500 + (taxable_income - 1000000) * 0.30
        return tax * 1.04


def format_salary_result(result: dict) -> str:
    """Format the salary calculation dict as a readable string for the agent."""
    if "error" in result:
        return f"⚠️ Calculation Error: {result['error']}"

    d = result["deductions"]
    ctc_lpa = result['ctc_annual'] / 100000
    inhand_lpa = result['inhand_annual'] / 100000

    output = f"""
📊 **Salary Breakdown for ₹{ctc_lpa:.1f} LPA CTC**

**Monthly Components:**
• Basic Salary: ₹{result['basic_monthly']:,}
• HRA: ₹{result['hra_monthly']:,}
• Special Allowance: ₹{result['special_allowance_monthly']:,}
• Gross Monthly: ₹{result['gross_monthly']:,}

**Monthly Deductions:**
• Employee PF (12% of Basic): ₹{d['employee_pf_monthly']:,}
• Professional Tax ({result['state'].title()}): ₹{d['professional_tax_monthly']:,}
• TDS (estimated, {result['tax_regime'].title()} Regime): ₹{d['tds_monthly']:,}
• **Total Deductions: ₹{d['total_deductions_monthly']:,}**

**✅ Estimated In-Hand Salary: ₹{result['inhand_monthly']:,}/month**
(₹{inhand_lpa:.2f} LPA annually)

**Additional Info:**
• Employer PF (in your CTC, not deducted from you): ₹{result['employer_pf_monthly']:,}/month
• Effective Tax Rate: {result['effective_tax_rate_percent']}%
• Tax Regime: {result['tax_regime'].title()} Tax Regime
""".strip()

    if result.get("variable_ctc_annual", 0) > 0:
        output += f"\n\n⚠️ {result['note']}"

    return output


# TOOL 2: Parse salary query from natural language

def parse_salary_query(question: str) -> Optional[dict]:
    """
    Extract CTC and parameters from a natural language salary question.
    Returns dict or None if no salary query detected.
    """
    question_lower = question.lower()

    # Detect if this is a salary calculation request
    salary_triggers = [
        "in-hand", "inhand", "in hand", "take home", "take-home",
        "calculate", "salary for", "salary if", "earning", "per month",
        "lpa", "lakhs per annum", "lakh per annum", "ctc is", "ctc of",
        "package of", "package is"
    ]
    if not any(t in question_lower for t in salary_triggers):
        return None

    # Extract CTC amount
    # Matches: "6 lpa", "6.5 lpa", "6 lakhs", "600000", "6,00,000"
    lpa_match = re.search(r'(\d+(?:\.\d+)?)\s*(?:lpa|l\.p\.a|lakhs?\s*per\s*annum|lakh)', question_lower)
    raw_match = re.search(r'(\d[\d,]+)', question_lower)

    ctc = None
    if lpa_match:
        ctc = float(lpa_match.group(1)) * 100000
    elif raw_match:
        raw = raw_match.group(1).replace(",", "")
        val = float(raw)
        # Heuristic: if val < 1000, assume it's in LPA
        ctc = val * 100000 if val < 1000 else val

    if ctc is None:
        return None

    # Extract variable pay
    var_match = re.search(r'(\d+(?:\.\d+)?)\s*%?\s*variable', question_lower)
    variable_percent = float(var_match.group(1)) if var_match else 0.0

    # Extract state
    state = "karnataka"  # default Bangalore
    for s in PROFESSIONAL_TAX_BY_STATE:
        if s in question_lower:
            state = s
            break
    for s in NO_PT_STATES:
        if s in question_lower:
            state = s
            break

    # Tax regime
    tax_regime = "new"
    if "old regime" in question_lower or "old tax" in question_lower:
        tax_regime = "old"

    # Metro
    metro_cities = ["mumbai", "delhi", "bangalore", "bengaluru", "chennai", "kolkata", "hyderabad"]
    is_metro = any(city in question_lower for city in metro_cities) or True  # default metro

    return {
        "ctc_annual": ctc,
        "variable_percent": variable_percent,
        "state": state,
        "tax_regime": tax_regime,
        "is_metro": is_metro,
    }


# TOOL 3: Current date context

def get_current_financial_context() -> str:
    """Returns the current financial year context."""
    now = datetime.now()
    year = now.year
    month = now.month
    if month >= 4:
        fy = f"FY{year}-{str(year+1)[2:]}"
    else:
        fy = f"FY{year-1}-{str(year)[2:]}"

    return (
        f"Current date: {now.strftime('%B %d, %Y')}. "
        f"Current Financial Year: {fy}. "
        f"ITR filing deadline for salaried employees: July 31, {year if month < 8 else year+1}."
    )
