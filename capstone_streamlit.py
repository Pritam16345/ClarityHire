"""
capstone_streamlit.py — Production Streamlit UI for First-Time Job Seeker Bot
Run: streamlit run capstone_streamlit.py
"""

import streamlit as st
import uuid
import time
import os

# Page configuration

st.set_page_config(
    page_title="ClarityHire",
    page_icon="◼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# CSS styling

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

/* ── Design Tokens ──────────────────────────────────────────────────────── */
:root {
    --bg: #0d0d0d;
    --surface: #ffffff;
    --surface-dark: #181818;
    --surface-alt: #f7f7f7;
    --border: #d4d4d4;
    --border-light: #ebebeb;
    --border-dark: #2a2a2a;
    --text: #1a1a1a;
    --text-on-dark: #e5e5e5;
    --text-muted-dark: #737373;
    --text-secondary: #525252;
    --text-muted: #8c8c8c;
    --accent: #ffffff;
    --accent-hover: #e0e0e0;
    --sidebar-bg: #0a0a0a;
    --sidebar-surface: #161616;
    --sidebar-surface-hover: #1e1e1e;
    --sidebar-border: #252525;
    --sidebar-text: #d4d4d4;
    --sidebar-muted: #5a5a5a;
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 20px;
    --shadow-xs: 0 1px 2px rgba(0,0,0,0.15);
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.2);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.25);
    --shadow-lg: 0 8px 24px rgba(0,0,0,0.3);
    --transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

/* ── Global ─────────────────────────────────────────────────────────────── */
html, body, .stApp {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    background-color: var(--bg) !important;
    color: var(--text-on-dark) !important;
}

#MainMenu, footer, header { visibility: hidden !important; height: 0 !important; }
.stDeployButton { display: none !important; }

/* Scrollbar */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #555; }

/* ── Container — centered ───────────────────────────────────────────────── */
/* Force main content to center regardless of sidebar */
.stMain, [data-testid="stMain"] {
    margin-left: auto !important;
    margin-right: auto !important;
    width: 100% !important;
}
.stMain .block-container,
[data-testid="stMain"] .block-container,
[data-testid="stAppViewBlockContainer"] {
    padding-top: 1.5rem !important;
    padding-bottom: 0 !important;
    max-width: 860px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* ── Sidebar ────────────────────────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: var(--sidebar-bg) !important;
    border-right: 1px solid var(--sidebar-border) !important;
    width: 300px !important;
    min-width: 300px !important;
}
section[data-testid="stSidebar"] > div:first-child {
    padding: 1.5rem 1.25rem !important;
    background: var(--sidebar-bg) !important;
}
section[data-testid="stSidebar"] * {
    color: var(--sidebar-text) !important;
    font-family: 'Inter', sans-serif !important;
}
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3 {
    color: #ffffff !important;
    font-weight: 600 !important;
    letter-spacing: -0.01em !important;
    font-size: 1.15rem !important;
}
section[data-testid="stSidebar"] hr {
    border-color: var(--sidebar-border) !important;
    margin: 1rem 0 !important;
}
/* Sidebar label text */
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stNumberInput label,
section[data-testid="stSidebar"] .stSlider label {
    color: var(--sidebar-muted) !important;
    font-size: 0.72rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.06em !important;
}

/* ── Sidebar Inputs — Professional Block Style ──────────────────────────── */
section[data-testid="stSidebar"] .stNumberInput > div > div > input {
    background: var(--sidebar-surface) !important;
    border: 1px solid var(--sidebar-border) !important;
    color: #ffffff !important;
    border-radius: var(--radius-sm) !important;
    padding: 0.6rem 0.75rem !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
    transition: var(--transition) !important;
}
section[data-testid="stSidebar"] .stNumberInput > div > div > input:focus {
    border-color: #ffffff !important;
    box-shadow: 0 0 0 1px rgba(255,255,255,0.15) !important;
}
/* Number input +/- buttons */
section[data-testid="stSidebar"] .stNumberInput button {
    background: var(--sidebar-surface) !important;
    border: 1px solid var(--sidebar-border) !important;
    color: var(--sidebar-text) !important;
    border-radius: var(--radius-sm) !important;
    transition: var(--transition) !important;
}
section[data-testid="stSidebar"] .stNumberInput button:hover {
    background: var(--sidebar-surface-hover) !important;
    border-color: #ffffff !important;
}

/* Selectbox / Dropdown */
section[data-testid="stSidebar"] .stSelectbox > div > div {
    background: var(--sidebar-surface) !important;
    border: 1px solid var(--sidebar-border) !important;
    color: #ffffff !important;
    border-radius: var(--radius-sm) !important;
    padding: 0.1rem 0 !important;
    transition: var(--transition) !important;
    cursor: pointer !important;
}
section[data-testid="stSidebar"] .stSelectbox > div > div:hover {
    border-color: #555 !important;
}
section[data-testid="stSidebar"] .stSelectbox [data-testid="stMarkdownContainer"] {
    color: #ffffff !important;
}
/* Dropdown arrow */
section[data-testid="stSidebar"] .stSelectbox svg {
    fill: var(--sidebar-muted) !important;
}

/* Slider */
section[data-testid="stSidebar"] .stSlider [data-testid="stThumbValue"] {
    color: #ffffff !important;
    font-weight: 600 !important;
}
section[data-testid="stSidebar"] .stSlider [data-testid="stTickBarMin"],
section[data-testid="stSidebar"] .stSlider [data-testid="stTickBarMax"] {
    color: var(--sidebar-muted) !important;
}
/* Slider track */
section[data-testid="stSidebar"] .stSlider > div > div > div > div {
    background: var(--sidebar-border) !important;
}

/* ── Sidebar Metrics — Block Cards ──────────────────────────────────────── */
section[data-testid="stSidebar"] [data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-weight: 700 !important;
    font-size: 1.3rem !important;
}
section[data-testid="stSidebar"] [data-testid="stMetricLabel"] {
    color: var(--sidebar-muted) !important;
    font-size: 0.68rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.06em !important;
}

/* ── Sidebar Buttons ────────────────────────────────────────────────────── */
section[data-testid="stSidebar"] .stButton > button[kind="primary"],
section[data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"] {
    background: #ffffff !important;
    color: #000000 !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    font-weight: 600 !important;
    font-size: 0.85rem !important;
    padding: 0.6rem 1rem !important;
    transition: var(--transition) !important;
    letter-spacing: 0.01em !important;
}
section[data-testid="stSidebar"] .stButton > button[kind="primary"]:hover,
section[data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"]:hover {
    background: #e0e0e0 !important;
    transform: translateY(-1px) !important;
}

section[data-testid="stSidebar"] .stButton > button[kind="secondary"],
section[data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-secondary"] {
    background: var(--sidebar-surface) !important;
    color: var(--sidebar-text) !important;
    border: 1px solid var(--sidebar-border) !important;
    border-radius: var(--radius-sm) !important;
    font-weight: 500 !important;
    font-size: 0.85rem !important;
    padding: 0.6rem 1rem !important;
    transition: var(--transition) !important;
}
section[data-testid="stSidebar"] .stButton > button[kind="secondary"]:hover,
section[data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-secondary"]:hover {
    background: var(--sidebar-surface-hover) !important;
    border-color: #555 !important;
}

/* ── Sidebar Alert / Success ────────────────────────────────────────────── */
section[data-testid="stSidebar"] .stAlert,
section[data-testid="stSidebar"] [data-testid="stNotification"] {
    background: var(--sidebar-surface) !important;
    border: 1px solid var(--sidebar-border) !important;
    color: var(--sidebar-text) !important;
    border-radius: var(--radius-sm) !important;
}

/* ── Sidebar Toggle — CLOSE button (inside sidebar top-right) ───────────── */
button[data-testid="stBaseButton-headerNoPadding"],
button[data-testid="stSidebarCollapseButton"],
section[data-testid="stSidebar"] button[kind="header"] {
    background: var(--sidebar-surface) !important;
    border: 1px solid var(--sidebar-border) !important;
    border-radius: var(--radius-sm) !important;
    color: #ffffff !important;
    width: 34px !important;
    height: 34px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    transition: var(--transition) !important;
    position: relative !important;
    z-index: 999 !important;
    margin: 0 !important;
    padding: 0 !important;
    font-size: 0 !important;
    overflow: hidden !important;
}
button[data-testid="stBaseButton-headerNoPadding"]:hover,
button[data-testid="stSidebarCollapseButton"]:hover,
section[data-testid="stSidebar"] button[kind="header"]:hover {
    background: #333 !important;
    border-color: #555 !important;
}
button[data-testid="stBaseButton-headerNoPadding"] *,
button[data-testid="stSidebarCollapseButton"] *,
section[data-testid="stSidebar"] button[kind="header"] * {
    font-size: 0 !important;
    visibility: hidden !important;
    width: 0 !important;
    height: 0 !important;
    overflow: hidden !important;
}
button[data-testid="stBaseButton-headerNoPadding"]::after,
button[data-testid="stSidebarCollapseButton"]::after,
section[data-testid="stSidebar"] button[kind="header"]::after {
    content: '✕' !important;
    font-size: 15px !important;
    color: #ffffff !important;
    display: flex !important;
    visibility: visible !important;
    width: auto !important;
    height: auto !important;
    align-items: center !important;
    justify-content: center !important;
}

/* ── Sidebar Toggle — OPEN button (floating pill on left edge) ──────────── */
[data-testid="collapsedControl"] {
    position: fixed !important;
    left: 0 !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    z-index: 99999 !important;
    background: #1a1a1a !important;
    border: 1px solid #333 !important;
    border-left: none !important;
    border-radius: 0 12px 12px 0 !important;
    width: 32px !important;
    height: 72px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    transition: var(--transition) !important;
    padding: 0 !important;
    box-shadow: 4px 0 12px rgba(0,0,0,0.3) !important;
    overflow: hidden !important;
}
[data-testid="collapsedControl"]:hover {
    background: #2a2a2a !important;
    width: 38px !important;
    border-color: #555 !important;
}
[data-testid="collapsedControl"] button {
    background: transparent !important;
    border: none !important;
    color: #ffffff !important;
    font-size: 0 !important;
    width: 100% !important;
    height: 100% !important;
    cursor: pointer !important;
    padding: 0 !important;
    overflow: hidden !important;
}
[data-testid="collapsedControl"] button * {
    font-size: 0 !important;
    visibility: hidden !important;
    width: 0 !important;
    height: 0 !important;
    overflow: hidden !important;
}
[data-testid="collapsedControl"] button::after {
    content: '☰' !important;
    font-size: 18px !important;
    color: #ffffff !important;
    display: flex !important;
    visibility: visible !important;
    width: auto !important;
    height: auto !important;
    align-items: center !important;
    justify-content: center !important;
}

/* ── Header Card — Premium ──────────────────────────────────────────────── */
.jl-header {
    background: var(--surface-dark);
    border: 1px solid var(--border-dark);
    padding: 2.25rem 2.5rem;
    border-radius: var(--radius-xl);
    margin-bottom: 1.75rem;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-md);
}
.jl-header::before {
    content: '';
    position: absolute;
    top: -80px; right: -40px;
    width: 250px; height: 250px;
    background: radial-gradient(circle, rgba(255,255,255,0.025) 0%, transparent 70%);
    border-radius: 50%;
}
.jl-header::after {
    content: '';
    position: absolute;
    bottom: -60px; left: 15%;
    width: 180px; height: 180px;
    background: radial-gradient(circle, rgba(255,255,255,0.015) 0%, transparent 70%);
    border-radius: 50%;
}
/* Logo lockup */
.jl-logo {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    margin-bottom: 0.65rem;
}
.jl-logo-icon {
    width: 40px; height: 40px;
    background: #ffffff;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem;
    color: #000000;
    font-weight: 800;
    font-family: 'Inter', sans-serif;
    flex-shrink: 0;
    box-shadow: 0 2px 8px rgba(255,255,255,0.08);
}
.jl-logo-text {
    font-family: 'Playfair Display', serif;
    font-size: 1.75rem;
    font-weight: 600;
    color: #ffffff;
    letter-spacing: -0.02em;
    line-height: 1;
}
.jl-badge {
    display: inline-block;
    background: rgba(255,255,255,0.06);
    color: rgba(255,255,255,0.4);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 0.2rem 0.75rem;
    border-radius: 99px;
    font-size: 0.63rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-top: 0.5rem;
}
.jl-header p {
    color: rgba(255,255,255,0.4);
    margin: 0.65rem 0 0 0;
    font-size: 0.86rem;
    font-weight: 300;
    line-height: 1.55;
    max-width: 540px;
}

/* ── Starter Prompt Cards ───────────────────────────────────────────────── */
.starter-label {
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--text-muted-dark);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.85rem;
}

div[data-testid="stHorizontalBlock"] .stButton > button {
    background: var(--surface-dark) !important;
    color: #e5e5e5 !important;
    border: 1px solid var(--border-dark) !important;
    border-radius: var(--radius-md) !important;
    padding: 0.9rem 1.1rem !important;
    font-size: 0.85rem !important;
    font-weight: 400 !important;
    font-family: 'Inter', sans-serif !important;
    text-align: left !important;
    transition: var(--transition) !important;
    box-shadow: var(--shadow-xs) !important;
    line-height: 1.5 !important;
    min-height: 3.2rem !important;
}
/* Ensure button text (spans, paragraphs inside) is also visible */
div[data-testid="stHorizontalBlock"] .stButton > button p,
div[data-testid="stHorizontalBlock"] .stButton > button span {
    color: #e5e5e5 !important;
}
div[data-testid="stHorizontalBlock"] .stButton > button:hover {
    background: #ffffff !important;
    color: #000000 !important;
    border-color: #ffffff !important;
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-md) !important;
}
div[data-testid="stHorizontalBlock"] .stButton > button:hover p,
div[data-testid="stHorizontalBlock"] .stButton > button:hover span {
    color: #000000 !important;
}

/* ── Chat Container Card ───────────────────────────────────────────────── */
.chat-container {
    background: var(--surface-dark);
    border: 1px solid var(--border-dark);
    border-radius: var(--radius-xl);
    padding: 1.5rem 1.75rem;
    margin-bottom: 1rem;
    box-shadow: var(--shadow-sm);
    min-height: 120px;
}

/* User message */
.user-row {
    display: flex;
    justify-content: flex-end;
    align-items: flex-start;
    margin: 1.15rem 0;
    gap: 0.6rem;
}
.user-avatar {
    width: 30px; height: 30px; min-width: 30px;
    background: #ffffff;
    color: #000000;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.65rem; font-weight: 700;
    flex-shrink: 0;
    margin-top: 3px;
}
.user-bubble {
    background: #ffffff;
    color: #000000;
    padding: 0.8rem 1.1rem;
    border-radius: var(--radius-lg) var(--radius-lg) 4px var(--radius-lg);
    max-width: 72%;
    font-size: 0.9rem;
    line-height: 1.6;
    font-weight: 400;
}

/* Bot message */
.bot-row {
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    margin: 1.15rem 0;
    gap: 0.6rem;
}
.bot-avatar {
    width: 30px; height: 30px; min-width: 30px;
    background: #252525;
    border: 1px solid #333;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.7rem;
    color: #ffffff;
    flex-shrink: 0;
    margin-top: 3px;
}
.bot-bubble {
    background: #1e1e1e;
    border: 1px solid #2a2a2a;
    padding: 0.95rem 1.2rem;
    border-radius: 4px var(--radius-lg) var(--radius-lg) var(--radius-lg);
    max-width: 80%;
    font-size: 0.9rem;
    line-height: 1.75;
    color: var(--text-on-dark);
}
.bot-bubble strong { font-weight: 600; color: #ffffff; }
.bot-bubble ul, .bot-bubble ol { margin: 0.5rem 0; padding-left: 1.2rem; }
.bot-bubble li { margin-bottom: 0.2rem; }

/* Meta bar */
.bot-meta {
    display: flex;
    align-items: center;
    gap: 0.4rem;
    flex-wrap: wrap;
    margin-bottom: 0.45rem;
}

/* Source & badges */
.source-pill {
    display: inline-block;
    background: #252525;
    color: #a0a0a0;
    border: 1px solid #333;
    padding: 0.15rem 0.55rem;
    border-radius: 99px;
    font-size: 0.68rem;
    font-weight: 500;
    margin: 0.1rem 0.05rem;
}
.faith-badge {
    display: inline-block;
    padding: 0.15rem 0.55rem;
    border-radius: 99px;
    font-size: 0.68rem;
    font-weight: 600;
}
.faith-high { background: #0a2e1a; color: #4ade80; border: 1px solid #166534; }
.faith-mid  { background: #2e1e0a; color: #fbbf24; border: 1px solid #92400e; }
.faith-low  { background: #2e0a0a; color: #f87171; border: 1px solid #991b1b; }
.route-badge {
    display: inline-block;
    background: #252525;
    color: #999;
    border: 1px solid #333;
    padding: 0.12rem 0.5rem;
    border-radius: 99px;
    font-size: 0.66rem;
    font-weight: 600;
}

/* Thinking animation */
.thinking-row {
    display: flex;
    justify-content: flex-start;
    align-items: flex-start;
    margin: 1rem 0;
    gap: 0.6rem;
}
.thinking-dots {
    background: #1e1e1e;
    border: 1px solid #2a2a2a;
    padding: 0.8rem 1.2rem;
    border-radius: 4px var(--radius-lg) var(--radius-lg) var(--radius-lg);
    font-size: 0.85rem;
    color: var(--text-muted-dark);
    display: flex;
    align-items: center;
    gap: 0.3rem;
}
@keyframes blink {
    0%, 80%, 100% { opacity: 0.2; }
    40% { opacity: 1; }
}
.dot { animation: blink 1.4s infinite both; color: #888; }
.dot:nth-child(2) { animation-delay: 0.2s; }
.dot:nth-child(3) { animation-delay: 0.4s; }

/* Follow-up */
.followup-container {
    margin-top: 1rem;
    padding-top: 0.85rem;
    border-top: 1px solid var(--border-dark);
}
.followup-label {
    font-size: 0.7rem;
    color: var(--text-muted-dark);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.45rem;
}

/* ── Input Area ─────────────────────────────────────────────────────────── */
.stTextInput > div > div > input {
    border-radius: var(--radius-lg) !important;
    border: 1px solid var(--border-dark) !important;
    padding: 0.8rem 1rem !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.9rem !important;
    transition: var(--transition) !important;
    background: var(--surface-dark) !important;
    color: var(--text-on-dark) !important;
    box-shadow: none !important;
}
.stTextInput > div > div > input:focus {
    border-color: #555 !important;
    box-shadow: 0 0 0 1px rgba(255,255,255,0.08) !important;
}
.stTextInput > div > div > input::placeholder {
    color: var(--text-muted-dark) !important;
    font-weight: 300 !important;
}

/* ── Main area buttons ──────────────────────────────────────────────────── */
.stButton > button[kind="primary"],
.stButton > button[data-testid="stBaseButton-primary"] {
    background: #ffffff !important;
    color: #000000 !important;
    border: none !important;
    border-radius: var(--radius-md) !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    transition: var(--transition) !important;
    box-shadow: var(--shadow-xs) !important;
}
.stButton > button[kind="primary"]:hover,
.stButton > button[data-testid="stBaseButton-primary"]:hover {
    background: #e0e0e0 !important;
    transform: translateY(-1px) !important;
    box-shadow: var(--shadow-sm) !important;
}
/* Override for sidebar primary buttons (already handled above) */

/* ── Sidebar topic list ─────────────────────────────────────────────────── */
.sb-section {
    font-size: 0.65rem;
    font-weight: 600;
    color: var(--sidebar-muted);
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 0.6rem;
    margin-top: 0.15rem;
}
.sb-topic {
    font-size: 0.8rem;
    padding: 0.28rem 0;
    color: var(--sidebar-text);
    display: flex;
    align-items: center;
    gap: 0.45rem;
}
.sb-dot {
    width: 3px; height: 3px;
    background: var(--sidebar-muted);
    border-radius: 50%;
    flex-shrink: 0;
}

/* ── Sidebar Stat Block ─────────────────────────────────────────────────── */
.stat-block {
    background: var(--sidebar-surface);
    border: 1px solid var(--sidebar-border);
    border-radius: var(--radius-sm);
    padding: 0.7rem 0.85rem;
    margin-bottom: 0.5rem;
}
.stat-label {
    font-size: 0.62rem;
    font-weight: 600;
    color: var(--sidebar-muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.15rem;
}
.stat-value {
    font-size: 1.2rem;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.02em;
}

/* ── Footer ─────────────────────────────────────────────────────────────── */
.jl-footer {
    margin-top: 3rem;
    padding: 1.5rem 0 1.25rem;
    border-top: 1px solid var(--border-dark);
    text-align: center;
}
.jl-footer-inner { max-width: 550px; margin: 0 auto; }
.jl-footer-brand {
    font-family: 'Playfair Display', serif;
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-on-dark);
    margin-bottom: 0.3rem;
}
.jl-footer-copy {
    font-size: 0.72rem;
    color: var(--text-muted-dark);
    margin: 0.25rem 0;
}
.jl-footer-links {
    display: flex;
    justify-content: center;
    gap: 1.25rem;
    margin: 0.55rem 0;
    flex-wrap: wrap;
}
.jl-footer-links span {
    font-size: 0.68rem;
    color: var(--text-muted-dark);
    font-weight: 500;
}
.jl-footer-line {
    width: 32px; height: 1px;
    background: var(--border-dark);
    margin: 0.65rem auto;
}
.jl-footer-disclaimer {
    font-size: 0.66rem;
    color: var(--text-muted-dark);
    line-height: 1.5;
    max-width: 440px;
    margin: 0 auto;
    font-style: italic;
}
.jl-footer-version {
    font-size: 0.63rem;
    color: #444;
    margin-top: 0.6rem;
    letter-spacing: 0.03em;
}

/* Section divider */
.section-divider {
    border: none;
    border-top: 1px solid var(--border-dark);
    margin: 1.5rem 0;
}
</style>
""", unsafe_allow_html=True)


# Agent initialization

@st.cache_resource
def load_agent():
    from agent import build_agent
    app, collection, embedder = build_agent()
    return app, collection, embedder


# Session state

def init_session():
    defaults = {
        "messages": [],
        "thread_id": str(uuid.uuid4()),
        "question_count": 0,
        "follow_ups": [],
        "pending_question": None,
        "user_name": "",
        "processing": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_session()


# Sidebar panel

with st.sidebar:
    st.markdown("## ◼ ClarityHire")
    st.markdown(
        "<span style='font-size:0.78rem;color:#555;font-weight:300;'>"
        "Offer Letter Intelligence</span>",
        unsafe_allow_html=True,
    )
    st.markdown("---")

    # Capabilities list
    st.markdown("<div class='sb-section'>Capabilities</div>", unsafe_allow_html=True)
    for t in [
        "CTC & Salary Breakdown",
        "PF, TDS, Professional Tax",
        "In-Hand Salary Calculator",
        "Offer Letter Red Flags",
        "Legal Rights & Notice Period",
        "Leave Policy & Gratuity",
        "Background Verification",
        "Salary Negotiation Tips",
        "Variable Pay & ESOPs",
        "Probation & Confirmation",
    ]:
        st.markdown(
            f"<div class='sb-topic'><div class='sb-dot'></div>{t}</div>",
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Session Stats
    st.markdown("<div class='sb-section'>Session</div>", unsafe_allow_html=True)
    bot_msgs = [m for m in st.session_state.messages if m["role"] == "assistant"]
    avg_faith = (
        sum(m.get("faithfulness", 1.0) for m in bot_msgs) / max(len(bot_msgs), 1)
    )
    st.markdown(f"""
    <div style="display:flex;gap:0.5rem;">
        <div class="stat-block" style="flex:1;">
            <div class="stat-label">Questions</div>
            <div class="stat-value">{st.session_state.question_count}</div>
        </div>
        <div class="stat-block" style="flex:1;">
            <div class="stat-label">Faithfulness</div>
            <div class="stat-value">{avg_faith:.2f}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Quick Salary Calculator
    st.markdown("<div class='sb-section'>Quick Salary Check</div>", unsafe_allow_html=True)
    quick_ctc = st.number_input(
        "Annual CTC (₹)",
        min_value=0,
        max_value=50_000_000,
        step=100000,
        value=600000,
        help="Enter annual CTC in rupees. E.g. 600000 for 6 LPA",
    )
    quick_var = st.slider("Variable %", 0, 40, 0)
    quick_regime = st.selectbox("Tax Regime", ["new", "old"])
    quick_state = st.selectbox("State", [
        "karnataka", "maharashtra", "delhi", "telangana",
        "west bengal", "tamil nadu", "gujarat", "haryana",
    ])

    if st.button("Calculate", use_container_width=True, type="primary"):
        from tools import calculate_inhand_salary
        r = calculate_inhand_salary(
            ctc_annual=quick_ctc,
            variable_percent=quick_var,
            state=quick_state,
            tax_regime=quick_regime,
        )
        if "error" not in r:
            st.markdown(f"""
            <div class="stat-block" style="margin-top:0.5rem;">
                <div class="stat-label">Estimated In-Hand</div>
                <div class="stat-value">₹{r['inhand_monthly']:,}/mo</div>
                <div style="font-size:0.7rem;color:#666;margin-top:0.3rem;">
                    TDS ₹{r['deductions']['tds_monthly']:,} · PF ₹{r['deductions']['employee_pf_monthly']:,} · PT ₹{r['deductions']['professional_tax_monthly']:,}
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error(r["error"])

    st.markdown("---")

    # New Conversation button
    if st.button("New Conversation", use_container_width=True):
        for k in ["messages", "follow_ups", "pending_question", "user_name"]:
            st.session_state[k] = [] if k in ("messages", "follow_ups") else "" if k == "user_name" else None
        st.session_state.thread_id = str(uuid.uuid4())
        st.session_state.question_count = 0
        st.session_state.processing = False
        st.rerun()

    st.markdown("---")
    st.markdown(
        "<div style='font-size:0.68rem;color:#444;line-height:1.5;'>"
        "This assistant provides general information only. "
        "For binding financial or legal advice, consult a CA or HR professional."
        "</div>",
        unsafe_allow_html=True,
    )


# Main Header

st.markdown("""
<div class="jl-header">
    <div class="jl-logo">
        <div class="jl-logo-icon">CH</div>
        <div class="jl-logo-text">ClarityHire</div>
    </div>
    <p>Your intelligent guide to understanding job offers in India. Ask about CTC breakdowns, salary components, legal rights, and negotiation strategies.</p>
    <div class="jl-badge">Agentic RAG · LangGraph · ChromaDB</div>
</div>
""", unsafe_allow_html=True)


# Starter prompts

if not st.session_state.messages and not st.session_state.processing:
    st.markdown(
        "<div class='starter-label'>Suggested Questions</div>",
        unsafe_allow_html=True,
    )
    starters = [
        "Compute net monthly pay for 8 LPA in Bengaluru",
        "What is the difference between CTC and gross salary?",
        "How is PF calculated and is it included in my CTC?",
        "Are there any warning signs I should watch out for in this contract?",
        "My offer says 90 days notice period — is that normal for a fresher?",
        "What is a training bond and should I sign it?",
    ]
    starter_cols = st.columns(2, gap="medium")
    for i, prompt in enumerate(starters):
        col = starter_cols[i % 2]
        with col:
            if st.button(prompt, key=f"starter_{i}", use_container_width=True):
                st.session_state.pending_question = prompt
                st.rerun()

    st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)


# Chat history rendering

if st.session_state.messages or st.session_state.processing:
    chat_parts = ['<div class="chat-container">']

    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            chat_parts.append(f"""
            <div class="user-row">
                <div class="user-bubble">{msg['content']}</div>
                <div class="user-avatar">You</div>
            </div>""")
        else:
            sources = msg.get("sources", [])
            faithfulness = msg.get("faithfulness", 1.0)
            route = msg.get("route", "")

            if faithfulness >= 0.7:
                fc, fl = "faith-high", f"✓ {faithfulness:.2f}"
            elif faithfulness >= 0.5:
                fc, fl = "faith-mid", f"~ {faithfulness:.2f}"
            else:
                fc, fl = "faith-low", f"⚠ {faithfulness:.2f}"

            source_html = ""
            if sources:
                source_html = "<div style='margin-top:0.6rem;'>" + "".join(
                    f"<span class='source-pill'>{s}</span>" for s in sources
                ) + "</div>"

            route_badge = ""
            if route:
                rt = {"retrieve": "Knowledge Base", "tool": "Calculator", "memory_only": "Memory"}.get(route, route)
                route_badge = f"<span class='route-badge'>{rt}</span>"

            content = msg['content'].replace('\n', '<br>')

            chat_parts.append(f"""
            <div class="bot-row">
                <div class="bot-avatar">◼</div>
                <div class="bot-bubble">
                    <div class="bot-meta">
                        {route_badge}
                        <span class="faith-badge {fc}">Faithfulness {fl}</span>
                    </div>
                    {content}
                    {source_html}
                </div>
            </div>""")

    if st.session_state.processing:
        chat_parts.append("""
        <div class="thinking-row">
            <div class="bot-avatar">◼</div>
            <div class="thinking-dots">
                <span class="dot">●</span>
                <span class="dot">●</span>
                <span class="dot">●</span>
                <span style="margin-left:0.3rem;">Thinking</span>
            </div>
        </div>""")

    chat_parts.append('</div>')
    st.markdown("".join(chat_parts), unsafe_allow_html=True)

    # Follow-up suggestions
    if st.session_state.messages:
        last_msg = st.session_state.messages[-1]
        if last_msg["role"] == "assistant" and last_msg.get("follow_ups") and not st.session_state.processing:
            st.markdown(
                "<div class='followup-container'>"
                "<div class='followup-label'>You might also want to ask</div>"
                "</div>",
                unsafe_allow_html=True,
            )
            fu_cols = st.columns(min(len(last_msg["follow_ups"]), 3))
            for j, suggestion in enumerate(last_msg["follow_ups"][:3]):
                with fu_cols[j]:
                    if st.button(suggestion, key=f"followup_{j}", use_container_width=True):
                        st.session_state.pending_question = suggestion
                        st.rerun()


# Input area

st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
col_input, col_btn = st.columns([6, 1])
with col_input:
    user_input = st.text_input(
        "Ask anything about your offer letter...",
        key="chat_input",
        placeholder="Ask about salary, PF, notice period, red flags...",
        label_visibility="collapsed",
    )
with col_btn:
    send_clicked = st.button("Send →", type="primary", use_container_width=True)


# Process submitted question

# Handle pending question (from starter/follow-up buttons)
if st.session_state.pending_question:
    q = st.session_state.pending_question
    st.session_state.pending_question = None
    st.session_state.messages.append({"role": "user", "content": q})
    st.session_state.question_count += 1
    st.session_state.processing = True
    st.rerun()

# If processing flag is set, run the agent for the last user message
if st.session_state.processing:
    last_user_msgs = [m for m in st.session_state.messages if m["role"] == "user"]
    if last_user_msgs:
        question = last_user_msgs[-1]["content"]
        try:
            app, _, _ = load_agent()
            config = {"configurable": {"thread_id": st.session_state.thread_id}}
            initial_state = {
                "question": question,
                "messages": [
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                "route": "",
                "retrieved": "",
                "sources": [],
                "tool_result": "",
                "answer": "",
                "faithfulness": 0.0,
                "eval_retries": 0,
                "user_name": st.session_state.get("user_name", ""),
                "salary_inputs": {},
                "query_category": "",
                "follow_up_suggestions": [],
            }
            result = app.invoke(initial_state, config=config)
            answer = result.get("answer", "I could not generate a response.")
            extracted_name = result.get("user_name", "")
            if extracted_name:
                st.session_state.user_name = extracted_name
            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "sources": result.get("sources", []),
                "faithfulness": result.get("faithfulness", 1.0),
                "route": result.get("route", "retrieve"),
                "follow_ups": result.get("follow_up_suggestions", []),
            })
        except Exception as e:
            st.session_state.messages.append({
                "role": "assistant",
                "content": f"⚠️ Error: {str(e)}. Please try again.",
                "sources": [], "faithfulness": 0.0, "route": "", "follow_ups": [],
            })
        st.session_state.processing = False
        st.rerun()

# Handle text input
if (send_clicked or user_input) and user_input and not st.session_state.processing:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.question_count += 1
    st.session_state.processing = True
    st.rerun()


# Footer rendering

st.markdown("""
<div class="jl-footer">
    <div class="jl-footer-inner">
        <div class="jl-footer-brand">◼ ClarityHire</div>
        <div class="jl-footer-copy">© 2026 ClarityHire. All rights reserved.</div>
        <div class="jl-footer-links">
            <span>Privacy Policy</span>
            <span>Terms of Service</span>
            <span>Cookie Policy</span>
            <span>Accessibility</span>
        </div>
        <div class="jl-footer-line"></div>
        <div class="jl-footer-disclaimer">
            This tool is for informational purposes only and does not constitute financial, legal, or tax advice.
            Consult a qualified Chartered Accountant or legal professional before making employment decisions.
        </div>
        <div class="jl-footer-version">Built with LangGraph · Powered by Groq · v1.0.0</div>
    </div>
</div>
""", unsafe_allow_html=True)
