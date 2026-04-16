"""
Knowledge Base Documents — First-Time Job Seeker Assistant
15 focused documents, each covering ONE specific aspect.
Each document: 150–450 words, concrete facts, no filler.
"""

DOCUMENTS = [
    {
        "id": "doc_001",
        "topic": "CTC — What It Is and What It Includes",
        "text": """
CTC stands for Cost to Company. It is the total annual amount a company spends on an employee, including salary, allowances, and benefits. CTC is NOT the money you receive in your bank account — it is always higher than your take-home pay.

CTC is made up of two parts: Fixed CTC and Variable CTC. Fixed CTC is guaranteed every month. Variable CTC is performance-based and paid quarterly or annually only if targets are met. Many companies inflate their offered CTC by including variable components — always ask what percentage is fixed.

Typical CTC components:
- Basic Salary (usually 40–50% of CTC)
- House Rent Allowance (HRA) — usually 40–50% of Basic
- Special Allowance — the remaining amount after all other components
- Provident Fund (employer's contribution, 12% of Basic)
- Gratuity (4.81% of Basic, paid after 5 years)
- Medical Insurance Premium (company pays for you)
- Variable Pay / Performance Bonus

In-Hand Salary = CTC minus all deductions. Deductions include employee PF contribution, Professional Tax, TDS, and any loan EMI deductions. A CTC of 6 LPA may result in an in-hand salary of ₹38,000–₹42,000/month depending on your tax slab and city.

Always ask the HR for the exact salary breakup sheet before signing. The breakup determines your actual monthly income, your PF corpus, and your HRA tax exemption eligibility.
        """.strip()
    },
    {
        "id": "doc_002",
        "topic": "Basic Salary, HRA, and Special Allowance Explained",
        "text": """
Basic Salary is the foundation of your pay structure. All other components — HRA, PF, Gratuity — are calculated as a percentage of Basic. A higher Basic means higher PF deductions but also a larger retirement corpus and HRA tax benefit. Most companies set Basic at 40–50% of CTC.

House Rent Allowance (HRA) is given to cover rental expenses. It is typically 40% of Basic for non-metro cities and 50% of Basic for metro cities (Mumbai, Delhi, Kolkata, Chennai). HRA is partially tax-exempt if you actually pay rent. Tax exemption on HRA is the minimum of: (a) actual HRA received, (b) actual rent paid minus 10% of basic, or (c) 40%/50% of basic depending on city.

Dearness Allowance (DA) is mainly applicable in government jobs. In private sector, it is either zero or merged into Basic.

Special Allowance is the residual — whatever is left after allocating Basic, HRA, and other components. It is fully taxable with no exemptions.

Conveyance Allowance: Most companies now pay this as part of Special Allowance since the flat ₹1,600/month exemption was removed.

Medical Allowance: Previously ₹15,000/year was tax-free. This is now merged into the standard deduction of ₹50,000 under the new tax regime.

Key insight: Under the New Tax Regime (default from FY2024-25), most allowance exemptions are removed, but tax slabs are lower. Under Old Tax Regime, you keep exemptions like HRA, 80C, 80D but pay higher slab rates. Choosing the right regime can save ₹10,000–₹50,000 annually.
        """.strip()
    },
    {
        "id": "doc_003",
        "topic": "Provident Fund (PF) — Complete Guide",
        "text": """
Provident Fund (PF) is a mandatory retirement savings scheme governed by the Employees' Provident Fund Organisation (EPFO). It applies to all companies with 20 or more employees, and to employees earning a Basic Salary of up to ₹15,000/month. Companies may voluntarily extend it to higher-paid employees too.

Contribution rules:
- Employee contributes 12% of Basic Salary per month (deducted from your salary)
- Employer also contributes 12% of Basic Salary per month (this is part of your CTC)
- Of the employer's 12%: 8.33% goes to EPS (Employee Pension Scheme, capped at ₹1,250/month) and 3.67% goes to your EPF account

Interest rate: EPFO declares interest annually. It has been around 8.1–8.25% in recent years. PF interest is tax-free.

Example: If your Basic is ₹20,000/month:
- You contribute: ₹2,400/month (₹28,800/year)
- Employer contributes: ₹2,400/month (₹28,800/year)
- Your annual PF corpus growth: ~₹57,600 + interest

Tax treatment: PF contributions up to ₹1.5 lakh per year qualify for 80C deduction under Old Tax Regime. Withdrawals after 5 continuous years of service are tax-free.

UAAN (Universal Account Number): Your PF account is linked to your UAN. When you change jobs, transfer your PF using the EPFO portal — don't withdraw it prematurely as you lose both the corpus and the tax benefit.

Premature withdrawal: Allowed after 2 months of unemployment. But withdrawing before 5 years of service attracts TDS at 10% (if PAN linked) or 34.6% (if PAN not linked).
        """.strip()
    },
    {
        "id": "doc_004",
        "topic": "TDS on Salary — How It Works",
        "text": """
TDS stands for Tax Deducted at Source. Your employer deducts income tax from your salary every month and deposits it with the government on your behalf. At year end, you file an ITR and either get a refund or pay the remaining tax.

How it works: At the start of the financial year (April), your employer estimates your annual income and projects your total tax liability. This estimated tax is divided by 12 and deducted monthly. If your income changes mid-year (increment, bonus), the TDS is recalculated.

Tax slabs under New Tax Regime (FY2024-25, default):
- Up to ₹3 lakh: Nil
- ₹3–6 lakh: 5%
- ₹6–9 lakh: 10%
- ₹9–12 lakh: 15%
- ₹12–15 lakh: 20%
- Above ₹15 lakh: 30%
- Standard deduction: ₹75,000 (from FY2024-25)
- Rebate u/s 87A: If taxable income ≤ ₹7 lakh, tax is zero

Tax slabs under Old Tax Regime:
- Up to ₹2.5 lakh: Nil
- ₹2.5–5 lakh: 5%
- ₹5–10 lakh: 20%
- Above ₹10 lakh: 30%
- Plus deductions: 80C (₹1.5L), 80D (₹25K health insurance), HRA, etc.

Form 16: Issued by your employer every year (by June 15). It contains two parts — Part A (TDS deposited) and Part B (salary breakup and deductions). This is the primary document for filing your ITR.

Always declare your investments (PPF, ELSS, insurance premiums) to your employer by February so they reduce your TDS accordingly. Missing this means extra TDS is cut, and you get a refund only after filing ITR.
        """.strip()
    },
    {
        "id": "doc_005",
        "topic": "Professional Tax — State-Wise Rules",
        "text": """
Professional Tax (PT) is a state-level tax levied on individuals earning a salary. It is deducted by the employer from your monthly salary and deposited with the state government. Not all states levy Professional Tax.

States that levy Professional Tax (and their slabs):
- Maharashtra: ₹200/month for salary above ₹10,000 (₹300 in February = ₹2,500/year)
- Karnataka: ₹200/month for salary above ₹15,000
- West Bengal: ₹110–₹200/month depending on salary slab
- Telangana/Andhra Pradesh: ₹150–₹200/month
- Tamil Nadu: ₹75–₹208/month depending on slab
- Gujarat: ₹200/month for salary above ₹12,000

States with NO Professional Tax: Delhi, Haryana, Rajasthan, UP, Himachal Pradesh, Uttarakhand, Bihar, Jharkhand, Goa.

Maximum Professional Tax per year is capped at ₹2,500 as per the Constitution. PT is allowed as a deduction under Section 16(iii) — meaning if you pay ₹2,400 PT, it reduces your taxable income by ₹2,400 under Old Tax Regime.

For fresh graduates: If you start working in a PT-applicable state, expect ₹150–₹200 to be deducted monthly from day one. This is not a scam — check your payslip under "deductions" and verify it matches your state's official slab.
        """.strip()
    },
    {
        "id": "doc_006",
        "topic": "Gratuity — Eligibility and Calculation",
        "text": """
Gratuity is a one-time payment made by the employer to the employee as a token of appreciation for long service. It is governed by the Payment of Gratuity Act, 1972.

Eligibility: You must complete at least 5 continuous years of service with the same employer. There is one exception: if an employee dies or becomes disabled, gratuity is paid regardless of service duration.

Formula:
Gratuity = (Last Drawn Basic + DA) × 15/26 × Number of Years of Service

15/26 represents 15 working days out of 26 working days in a month.

Example: Basic = ₹30,000/month, Service = 7 years
Gratuity = ₹30,000 × (15/26) × 7 = ₹1,21,153

Tax exemption: Gratuity received by private sector employees is tax-free up to ₹20 lakh (under Section 10(10)).

Why it matters for freshers: Gratuity is included in your CTC as an annual component (4.81% of Basic). But you will NOT receive it unless you complete 5 years. If you leave before 5 years, you forfeit the gratuity entirely. This is a significant hidden cost of job-hopping early in your career.

Gratuity fund: Some companies maintain a separate gratuity fund (through LIC or trust). Others pay it from operating cash at the time of exit. Ask HR whether the company maintains a funded gratuity scheme.
        """.strip()
    },
    {
        "id": "doc_007",
        "topic": "Notice Period — What It Means and How to Handle It",
        "text": """
Notice period is the duration an employee must continue working after resigning before their last working day. It protects the employer from sudden workforce gaps.

Typical notice periods:
- Fresher / Junior roles (0–2 years): 30 days (1 month)
- Mid-level roles (2–5 years): 60 days (2 months)
- Senior roles (5+ years): 90 days (3 months)
- Specialized roles or managerial: Up to 6 months

Notice period buyout: If your new employer wants you to join sooner, you can pay your current employer an amount equal to your Basic salary for the remaining notice days. This is called a "notice period buyout." Some companies allow this; some don't. Read your offer letter carefully.

What happens if you don't serve notice: The company can hold your Full and Final Settlement (F&F), your experience letter, and your relieving letter. They may also take legal action for critical roles, though this is rare for junior positions.

New employer's notice period: Some companies offer a "notice period waiver" or will pay your buyout amount as part of the joining offer. This is negotiable — always ask.

Gardening leave: In some companies (especially BFSI and tech), after you resign, you are asked not to work but are paid for the notice period. This is called "gardening leave." You cannot join the competitor during this period.

Key clause to check: "Notice period can be extended at the discretion of management." This clause allows the company to extend your notice arbitrarily. Flag this during offer negotiation.
        """.strip()
    },
    {
        "id": "doc_008",
        "topic": "Probation Period — Rules and Implications",
        "text": """
Probation period is a trial period at the start of employment during which both the employer and employee assess fit. It typically lasts 3 to 6 months for freshers, and 6 months to 1 year for experienced hires.

During probation:
- You may receive a reduced salary or the same as offered (varies by company)
- Notice period is usually shorter — 15 days to 30 days instead of 60–90 days
- Employee benefits like medical insurance, PF enrollment, and leave accrual may be deferred or start from day one (check your offer letter)
- Performance review happens at the end of probation. If unsatisfactory, the company can extend probation or terminate.

Confirmation letter: After passing probation, you receive a confirmation letter. This formally makes you a permanent employee. Until then, you are a "probationer."

Important: Probation period counts toward your total service for Gratuity eligibility (5-year rule). So if your probation is 6 months, those months count.

Termination during probation: Legal rules around termination differ during probation. Employers generally have more flexibility to terminate without detailed cause during the probation period. This is legally valid in most states.

For freshers: Don't treat probation casually. Attendance, punctuality, and early deliverables during probation heavily influence your first appraisal and long-term growth trajectory in that company.
        """.strip()
    },
    {
        "id": "doc_009",
        "topic": "Variable Pay and Performance Bonus — How They Work",
        "text": """
Variable Pay (VP) is a performance-linked component of your CTC that is not guaranteed. It is paid out based on individual performance, team performance, or company performance — or a combination of all three.

Structure: Variable pay is typically expressed as a percentage of your Fixed CTC. For example: "CTC is ₹8 LPA with 15% variable" means ₹6.8 LPA fixed + ₹1.2 LPA variable. The ₹1.2 LPA is only paid if you achieve your KPIs.

Payout frequency: Variable pay is usually paid annually or quarterly. Many companies pay it in two tranches — half in Q2 and half at year end.

Payout conditions:
- Individual rating: Most schemes pay 100% variable only on a "meets expectations" or above rating
- Company performance: If the company does not hit targets, even a high performer may receive only 70–80% of their variable
- Cliff: Many variable schemes have a cliff — if your rating is below a threshold (e.g., below 2/5), you get zero variable, not a proportionate amount

Joining Bonus (Sign-On Bonus): A one-time payment made when you join. It almost always has a clawback clause — if you leave within 12–18 months, you must repay it. Read the clawback terms carefully. Clawback may be on gross amount or post-tax amount depending on the clause.

For freshers: Do not plan monthly expenses around variable pay. Treat it as a bonus when received, not as guaranteed income. Build your budget on fixed in-hand only.
        """.strip()
    },
    {
        "id": "doc_010",
        "topic": "Leave Policy — Types and Accrual Rules",
        "text": """
Leave policy defines how many paid days off you get, how they accrue, and under what conditions they can be taken or encashed.

Common leave types in Indian private sector:

Casual Leave (CL): 7–12 days/year. For short, unplanned absences. Usually not carried forward to next year.

Sick Leave (SL): 7–12 days/year. For medical reasons. Some companies require a doctor's certificate for SL beyond 2 consecutive days. Usually not encashable.

Earned Leave / Privilege Leave (EL/PL): 12–18 days/year. Accrues monthly (e.g., 1.25 days/month for 15 days/year). Can be accumulated up to a cap (usually 30–45 days) and is encashable at exit.

Maternity Leave: 26 weeks (6.5 months) for the first two children under the Maternity Benefit (Amendment) Act, 2017. Companies with 50+ employees must provide this.

Paternity Leave: No statutory requirement in India. Some companies offer 5–15 days voluntarily.

National and Festival Holidays: Typically 10–12 fixed national holidays (Republic Day, Independence Day, etc.) plus 5–10 optional festival holidays.

Loss of Pay (LOP): Any absence beyond your leave balance is marked as LOP. This deducts proportional salary: LOP deduction = (Monthly CTC / 26) × number of LOP days.

Accrual timing: Most companies accrue leave at the start of the year (full credit on January 1 or your joining anniversary) or monthly. Leaves taken before accrual creates a negative balance — if you resign with negative leave, it is deducted from your F&F.
        """.strip()
    },
    {
        "id": "doc_011",
        "topic": "ESOP and Joining Bonus — Clauses to Watch",
        "text": """
ESOPs (Employee Stock Option Plans) are options given to employees to purchase company shares at a pre-decided price (exercise price) in the future. They are a form of long-term compensation, common in startups and tech companies.

ESOP terminology:
- Grant: The company grants you X options on a specific date
- Vesting schedule: You earn the right to exercise options over time. A typical schedule is 4-year vesting with a 1-year cliff — meaning you get nothing if you leave before 1 year, 25% at 1 year, and the rest monthly/quarterly over 3 more years
- Exercise price: The price at which you can buy shares. If the company's current share price is higher, the ESOP has value
- Exercise window: After vesting, you have a window (typically 90 days after leaving) to exercise. Failing to exercise in time forfeits the options

ESOP value for freshers: ESOPs have real value only if the company has a successful IPO or acquisition. For early-stage startups, they may be worth zero. For late-stage or listed companies, they can add significant wealth.

Joining Bonus red flags:
- Clawback period: If you leave within 12–18 months, you repay the full joining bonus. Verify whether the clawback is on gross or net-of-tax amount.
- Condition of continuation: Some joining bonuses are conditional on completing 6 months — paid in two tranches (half at joining, half at 6 months).

Ask before signing: "Is the ESOP grant in addition to CTC or included in CTC?" Some companies count ESOP value in CTC at a notional rate, inflating the package number.
        """.strip()
    },
    {
        "id": "doc_012",
        "topic": "Red Flags in an Offer Letter",
        "text": """
Most fresh graduates sign offer letters without reading them carefully. These are the clauses that can hurt you:

1. Vague Variable Pay: "Variable pay is at management discretion" — with no formula or KPI definition. This means the company can pay zero without any recourse.

2. Extremely long notice period: Notice period of 90 days for a fresher role is unusual. It traps you and reduces your mobility. Negotiate it down to 30–60 days before joining.

3. Non-compete clause: "You cannot join a competitor for 12 months after leaving." The enforceability of non-compete clauses in India is legally weak for employees, but they create psychological pressure. Note it and seek legal advice if needed.

4. Mandatory bond / training bond: "You must work for X years or repay ₹Y toward training costs." Training bonds are enforceable in Indian courts if the training was genuine and the bond amount is reasonable. Avoid signing if the bond period is more than 1 year.

5. Clawback on joining bonus: Check whether it's gross or post-tax clawback. Gross clawback means you may owe money you never received after tax.

6. Offer letter vs. appointment letter: Offer letter is a preliminary document. The appointment letter (given on Day 1) is the binding contract. Ensure both documents match on CTC, designation, and joining date.

7. No salary breakup: If the offer letter only shows CTC without a component breakup, request the breakup before signing. The breakup determines your actual take-home.

8. Incorrect designation: Your designation affects visa applications, loan eligibility, and future job applications. Ensure it reflects your actual role.
        """.strip()
    },
    {
        "id": "doc_013",
        "topic": "Full and Final Settlement (F&F) — What Happens When You Leave",
        "text": """
Full and Final Settlement (F&F) is the financial settlement between you and your employer on the last day of employment. It includes all outstanding dues and recoveries.

What you receive in F&F:
- Salary for days worked in the last month
- Encashment of pending Earned Leave (EL/PL) balance
- Gratuity (if eligible — 5 years of service)
- Variable pay (pro-rated, if payout date has not passed)
- Reimbursement of pending expense claims

What may be deducted from F&F:
- Notice period shortfall (if you did not serve full notice)
- Loan or advance recovery
- Joining bonus clawback (if within clawback period)
- Negative leave balance (LOP recovery)
- Asset recovery (laptop, phone, etc. if not returned)

Timeline: Employers are legally required to process F&F within 45 days of your last working day. In practice, many delay it to 60–90 days. Follow up in writing (email) for a documented paper trail.

Documents received with F&F:
- Experience letter (states your tenure and designation)
- Relieving letter (confirms you have been relieved of all duties — required for your new employer's BGV)
- Form 16 / salary slips for the period worked
- PF transfer or withdrawal form

Important: Do not hand over company assets until you receive written confirmation of your F&F settlement. Keep copies of all correspondence.
        """.strip()
    },
    {
        "id": "doc_014",
        "topic": "Background Verification (BGV) — What Companies Check",
        "text": """
Background Verification (BGV) is conducted by most companies before or after joining. Failing BGV can result in offer revocation or termination even after months of working.

What is typically verified:
1. Education credentials: Degree certificate, marksheets, institution verification. Discrepancies in percentage, year of passing, or institution name are red flags.
2. Employment history: Previous employers are contacted to verify dates of joining and leaving, last designation, and eligibility for rehire.
3. Identity verification: Aadhaar, PAN, Passport.
4. Address verification: Permanent and current address.
5. Criminal record check: Police verification, court record check.
6. Reference check: 2–3 professional references contacted for feedback on work quality and conduct.

Common BGV failure reasons:
- Inflated percentage or CGPA on resume
- Wrong dates of employment (even by a few months)
- Designation mismatch (calling yourself "Senior Engineer" when you were "Engineer")
- Backlog suppression (claiming no backlogs when there were)

For freshers: Ensure your resume matches your marksheets exactly. CGPA to percentage conversion varies by university — use your official university formula, not a generic 9.5× formula.

BGV agencies: KPMG, AuthBridge, HireRight, FirstAdvantage are common agencies. The process takes 15–30 days. Your offer letter will include a BGV clause stating employment is conditional on satisfactory verification.
        """.strip()
    },
    {
        "id": "doc_015",
        "topic": "Negotiating Your First Salary — How to Do It Right",
        "text": """
Salary negotiation is expected and normal. Recruiters account for negotiation when making initial offers. Not negotiating is leaving money on the table.

What can be negotiated:
- Fixed CTC (most important)
- Joining date (gives you time to serve notice or take a break)
- Joining bonus (if you have a notice period buyout to pay)
- Designation (affects future job applications)
- Variable percentage (lower variable = more predictable income)

What is usually non-negotiable for freshers:
- PF and statutory benefits
- Leave policy
- Probation period

How to negotiate:
1. Get a competing offer or research market rates (use levels.fyi, AmbitionBox, Glassdoor for your role and city)
2. Quote a specific number, not a range. "I was expecting ₹7 LPA based on market benchmarks" is stronger than "I was hoping for something higher."
3. Justify with facts: your competing offer, your specific skills, your internship experience
4. Always negotiate over email or after verbal discussion — creates a paper trail

When NOT to negotiate: If the offer is already at or above market for a no-experience role, aggressive negotiation can create a negative impression. Read the situation.

Counteroffer from current employer: If you receive a counteroffer when resigning, statistics show 80%+ of employees who accept counteroffers leave within 12 months anyway. The root reasons for leaving rarely change.

Final rule: Never accept or reject an offer on the spot. Ask for 24–48 hours to review. This is professional and universally accepted.
        """.strip()
    }
]

# Metadata list for ChromaDB
METADATAS = [{"topic": doc["topic"], "id": doc["id"]} for doc in DOCUMENTS]
IDS = [doc["id"] for doc in DOCUMENTS]
TEXTS = [doc["text"] for doc in DOCUMENTS]
