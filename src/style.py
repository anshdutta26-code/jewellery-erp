import streamlit as st


BRAND_GREEN = "#103C2B"
BRAND_GREEN_DARK = "#0A2E22"
BRAND_GOLD = "#D2A33A"
BRAND_GOLD_LIGHT = "#E6C66E"
BRAND_IVORY = "#F8F3E8"
BRAND_PAPER = "#FFFDF8"
BRAND_SAGE = "#6C7C6A"


def inject_css() -> None:
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600&family=Montserrat:wght@400;500;600;700&display=swap');

        :root {
          --srj-green: #103C2B;
          --srj-green-dark: #0A2E22;
          --srj-gold: #D2A33A;
          --srj-gold-light: #E6C66E;
          --srj-ivory: #F8F3E8;
          --srj-paper: #FFFDF8;
          --srj-sage: #6C7C6A;
          --srj-border: rgba(210, 163, 58, .34);
        }

        html, body, [class*="st-"] {
          font-family: "Montserrat", sans-serif;
        }

        .stApp {
          background:
            radial-gradient(circle at 10% 14%, rgba(210,163,58,.10), transparent 18rem),
            radial-gradient(circle at 92% 18%, rgba(16,60,43,.07), transparent 20rem),
            radial-gradient(circle at 82% 85%, rgba(210,163,58,.07), transparent 22rem),
            linear-gradient(180deg, #FFFDF9 0%, #F8F3E8 100%);
          color: var(--srj-green-dark);
        }

        .block-container {
          padding-top: 1.45rem;
          padding-bottom: 3rem;
          max-width: 1480px;
        }

        /* Header / titles */
        .srj-eyebrow {
          color: var(--srj-gold);
          font-size: .70rem;
          letter-spacing: .26em;
          text-transform: uppercase;
          font-weight: 700;
          margin-bottom: .25rem;
        }

        .erp-title {
          color: var(--srj-green-dark);
          font-family: "Cormorant Garamond", Georgia, serif;
          font-size: 2.35rem;
          line-height: .98;
          font-weight: 700;
          letter-spacing: .005em;
          margin-bottom: .2rem;
        }

        .erp-sub {
          color: var(--srj-sage);
          font-size: .85rem;
          letter-spacing: .015em;
          margin-bottom: 1.25rem;
        }

        h1, h2, h3 {
          font-family: "Cormorant Garamond", Georgia, serif !important;
          color: var(--srj-green-dark) !important;
          letter-spacing: .01em !important;
        }

        h4, h5, h6 {
          color: var(--srj-green) !important;
        }


        .srj-seal {
          width: 156px;
          height: 156px;
          border-radius: 50%;
          margin: .15rem auto .85rem auto;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          background: radial-gradient(circle at 50% 38%, #173f30 0%, #0d2f23 72%);
          border: 1px solid rgba(230,198,110,.55);
          box-shadow: 0 12px 30px rgba(10,46,34,.14);
          color: var(--srj-gold-light);
        }

        .srj-monogram {
          font-family: "Cormorant Garamond", Georgia, serif;
          font-size: 3.05rem;
          line-height: .78;
          font-weight: 600;
          letter-spacing: -.06em;
        }

        .srj-name {
          margin-top: .55rem;
          font-family: "Cormorant Garamond", Georgia, serif;
          font-size: 1.02rem;
          font-weight: 700;
          letter-spacing: .11em;
        }

        .srj-jewels {
          font-size: .55rem;
          letter-spacing: .28em;
          margin-left: .28em;
          margin-top: .08rem;
        }

        .sidebar-brand {
          text-align: center;
          margin: .15rem 0 1rem 0;
          color: #E6C66E;
        }

        .sidebar-monogram {
          font-family: "Cormorant Garamond", Georgia, serif;
          font-size: 2.6rem;
          font-weight: 600;
          line-height: .9;
          letter-spacing: -.05em;
        }

        .sidebar-name {
          font-family: "Cormorant Garamond", Georgia, serif;
          font-size: 1.05rem;
          font-weight: 700;
          letter-spacing: .10em;
          margin-top: .28rem;
        }

        .sidebar-jewels {
          font-size: .52rem;
          letter-spacing: .24em;
          margin-top: .08rem;
          color: rgba(248,232,179,.82);
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
          background:
            radial-gradient(circle at 20% 0%, rgba(210,163,58,.09), transparent 13rem),
            linear-gradient(180deg, #123E2C 0%, #092C21 100%);
          border-right: 1px solid rgba(210,163,58,.45);
        }

        [data-testid="stSidebar"] [data-testid="stImage"] {
          max-width: 126px;
          margin: .25rem auto .6rem auto;
        }

        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] label {
          color: #F8E8B3 !important;
        }

        [data-testid="stSidebar"] [role="radiogroup"] {
          gap: .32rem;
        }

        [data-testid="stSidebar"] [role="radiogroup"] label {
          border: 1px solid transparent;
          border-radius: 8px;
          padding: .36rem .55rem;
          transition: all .15s ease;
        }

        [data-testid="stSidebar"] [role="radiogroup"] label:hover {
          background: rgba(210,163,58,.09);
          border-color: rgba(210,163,58,.20);
        }

        [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
          background: rgba(210,163,58,.16);
          border-color: rgba(230,198,110,.58);
          box-shadow: inset 3px 0 0 var(--srj-gold);
        }

        [data-testid="stSidebar"] hr {
          border-color: rgba(210,163,58,.25);
        }

        /* Metric cards */
        div[data-testid="stMetric"] {
          background: rgba(255,253,248,.94);
          border: 1px solid var(--srj-border);
          border-radius: 10px;
          padding: 14px 16px;
          box-shadow: 0 8px 24px rgba(20,55,39,.055);
          min-height: 112px;
        }

        div[data-testid="stMetric"] [data-testid="stMetricLabel"] p {
          color: var(--srj-sage) !important;
          text-transform: uppercase;
          letter-spacing: .12em;
          font-size: .66rem !important;
          font-weight: 700;
        }

        div[data-testid="stMetric"] [data-testid="stMetricValue"] {
          color: var(--srj-green-dark) !important;
          font-family: "Cormorant Garamond", Georgia, serif;
          font-weight: 700;
        }

        /* Forms / fields */
        [data-baseweb="input"] > div,
        [data-baseweb="select"] > div,
        [data-baseweb="textarea"] > div,
        [data-testid="stNumberInput"] input,
        [data-testid="stTextInput"] input,
        [data-testid="stTextArea"] textarea {
          background: #FFFDF8 !important;
          border-color: rgba(16,60,43,.18) !important;
          border-radius: 7px !important;
        }

        [data-testid="stTextInput"] input:focus,
        [data-testid="stNumberInput"] input:focus,
        [data-testid="stTextArea"] textarea:focus {
          border-color: var(--srj-gold) !important;
          box-shadow: 0 0 0 1px var(--srj-gold) !important;
        }

        [data-testid="stForm"] {
          background: rgba(255,253,248,.68);
          border: 1px solid rgba(210,163,58,.22);
          border-radius: 10px;
          padding: 1rem;
        }

        /* Buttons, inspired by website CTA */
        .stButton > button,
        [data-testid="stFormSubmitButton"] > button,
        .stDownloadButton > button {
          border-radius: 5px !important;
          min-height: 2.65rem;
          font-weight: 700 !important;
          letter-spacing: .10em !important;
          text-transform: uppercase;
          font-size: .72rem !important;
          border: 1px solid var(--srj-gold) !important;
          background: var(--srj-green) !important;
          color: #F7E8B7 !important;
          box-shadow: none !important;
        }

        .stButton > button:hover,
        [data-testid="stFormSubmitButton"] > button:hover,
        .stDownloadButton > button:hover {
          background: var(--srj-gold) !important;
          color: var(--srj-green-dark) !important;
          border-color: var(--srj-gold) !important;
        }

        /* Tabs match collection navigation */
        [data-baseweb="tab-list"] {
          gap: .15rem;
          border-bottom: 1px solid rgba(210,163,58,.28);
        }

        button[data-baseweb="tab"] {
          background: transparent !important;
          color: var(--srj-green) !important;
          text-transform: uppercase;
          letter-spacing: .11em;
          font-size: .72rem;
          font-weight: 600;
          padding-left: .9rem !important;
          padding-right: .9rem !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
          background: rgba(16,60,43,.06) !important;
          color: var(--srj-gold) !important;
          border-bottom: 2px solid var(--srj-gold) !important;
        }

        /* Tables / dataframes */
        [data-testid="stDataFrame"],
        [data-testid="stTable"] {
          border: 1px solid rgba(210,163,58,.26);
          border-radius: 8px;
          overflow: hidden;
          box-shadow: 0 6px 18px rgba(20,55,39,.035);
        }

        /* Alerts */
        [data-testid="stAlert"] {
          border-radius: 7px;
          border-left: 4px solid var(--srj-gold);
        }

        /* Login brand */
        .login-brand {
          text-align: center;
          max-width: 660px;
          margin: 0 auto .7rem auto;
        }

        .login-brand .tag {
          color: var(--srj-gold);
          text-transform: uppercase;
          letter-spacing: .24em;
          font-size: .69rem;
          font-weight: 700;
        }

        .login-brand .headline {
          font-family: "Cormorant Garamond", Georgia, serif;
          color: var(--srj-green-dark);
          font-size: 2.65rem;
          font-weight: 700;
          line-height: 1;
          margin: .18rem 0 .3rem 0;
        }

        .login-brand .strap {
          color: var(--srj-sage);
          font-size: .82rem;
        }

        .voucher-box {
          background: var(--srj-paper);
          border: 1px solid var(--srj-border);
          padding: 16px;
          border-radius: 9px;
        }

        .muted { color: var(--srj-sage); }

        @media (max-width: 800px) {
          .block-container { padding-top: .8rem; }
          .login-brand { padding-top: 4.6rem; }
          .erp-title { font-size: 1.95rem; }
          .login-brand .headline { font-size: 2.1rem; }
          div[data-testid="stMetric"] { min-height: 96px; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str = "") -> None:
    st.markdown('<div class="srj-eyebrow">SHUBHRAJ JEWELS · ERP</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="erp-title">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="erp-sub">{subtitle}</div>', unsafe_allow_html=True)
