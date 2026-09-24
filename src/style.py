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
          position: relative;
          overflow-x: hidden;
          background:
            radial-gradient(circle at 8% 10%, rgba(210,163,58,.12), transparent 18rem),
            radial-gradient(circle at 96% 18%, rgba(16,60,43,.08), transparent 22rem),
            radial-gradient(circle at 82% 82%, rgba(210,163,58,.08), transparent 24rem),
            linear-gradient(180deg, #FFFDF9 0%, #F8F3E8 100%);
          color: var(--srj-green-dark);
        }

        .stApp::before {
          content: "";
          position: fixed;
          inset: 0;
          pointer-events: none;
          z-index: 0;
          opacity: .22;
          background-image:
            linear-gradient(45deg, transparent 48%, rgba(210,163,58,.11) 49%, rgba(210,163,58,.11) 51%, transparent 52%),
            linear-gradient(-45deg, transparent 48%, rgba(210,163,58,.07) 49%, rgba(210,163,58,.07) 51%, transparent 52%);
          background-size: 74px 74px;
          mask-image: radial-gradient(circle at 50% 35%, black 0%, transparent 72%);
        }

        .block-container {
          position: relative;
          z-index: 1;
          padding-top: 4.6rem;
          padding-bottom: 3rem;
          max-width: 1480px;
        }

        /* Header / titles */
        .erp-hero {
          position: relative;
          overflow: hidden;
          margin: 0 0 1.2rem 0;
          padding: 1.35rem 1.5rem 1.25rem 1.5rem;
          border: 1px solid rgba(210,163,58,.58);
          border-radius: 10px;
          background:
            radial-gradient(circle at 90% 20%, rgba(230,198,110,.12), transparent 13rem),
            linear-gradient(135deg, #123E2C 0%, #0A2E22 74%);
          box-shadow: 0 12px 30px rgba(10,46,34,.10);
        }

        .erp-hero::after {
          content: "◇";
          position: absolute;
          right: 1.1rem;
          top: -.45rem;
          color: rgba(230,198,110,.12);
          font-family: Georgia, serif;
          font-size: 6.2rem;
          line-height: 1;
          transform: rotate(8deg);
        }

        .erp-hero .srj-eyebrow {
          color: var(--srj-gold-light);
        }

        .erp-hero .erp-title {
          color: #FFF8E6;
          margin-bottom: .35rem;
        }

        .erp-hero .erp-sub {
          color: rgba(255,248,230,.72);
          margin-bottom: 0;
        }

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
          margin: .55rem auto .9rem auto;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          background:
            url("https://raw.githubusercontent.com/anshdutta26-code/jewellery-erp/main/assets/srj_logo.png")
            center / cover no-repeat;
          border: 1px solid rgba(230,198,110,.55);
          box-shadow: 0 12px 30px rgba(10,46,34,.14);
          color: var(--srj-gold-light);
        }

        .srj-seal > * { visibility: hidden; }

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

        .sidebar-brand::before {
          content: "";
          display: block;
          width: 92px;
          height: 92px;
          border-radius: 50%;
          margin: 0 auto .55rem auto;
          background:
            url("https://raw.githubusercontent.com/anshdutta26-code/jewellery-erp/main/assets/srj_logo.png")
            center / cover no-repeat;
          border: 1px solid rgba(230,198,110,.48);
          box-shadow: 0 8px 18px rgba(0,0,0,.16);
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
          background: rgba(255,253,248,.88);
          border: 1px solid rgba(210,163,58,.30);
          border-radius: 10px;
          padding: 1rem;
          box-shadow: 0 10px 28px rgba(10,46,34,.045);
          backdrop-filter: blur(6px);
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
          gap: 0;
          padding: .18rem;
          border: 1px solid rgba(210,163,58,.34);
          border-radius: 7px;
          background: linear-gradient(180deg, #143F2E 0%, #0D3225 100%);
          box-shadow: 0 5px 16px rgba(10,46,34,.07);
        }

        button[data-baseweb="tab"] {
          background: transparent !important;
          color: rgba(255,248,230,.78) !important;
          text-transform: uppercase;
          letter-spacing: .10em;
          font-size: .70rem;
          font-weight: 600;
          border-radius: 5px !important;
          padding-left: 1rem !important;
          padding-right: 1rem !important;
        }

        button[data-baseweb="tab"]:hover {
          color: var(--srj-gold-light) !important;
          background: rgba(210,163,58,.08) !important;
        }

        button[data-baseweb="tab"][aria-selected="true"] {
          background: rgba(210,163,58,.12) !important;
          color: var(--srj-gold-light) !important;
          box-shadow: inset 0 -2px 0 var(--srj-gold);
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
          .block-container {
            padding-top: 7.1rem !important;
            padding-left: .95rem;
            padding-right: .95rem;
          }
          .srj-seal {
            width: 142px;
            height: 142px;
            margin-top: .25rem;
          }
          .srj-monogram { font-size: 2.75rem; }
          .erp-hero {
            padding: 1.05rem 1rem;
            border-radius: 8px;
          }
          .erp-title { font-size: 1.95rem; }
          .login-brand .headline { font-size: 2.1rem; }
          .login-brand .tag {
            font-size: .62rem;
            letter-spacing: .19em;
          }
          div[data-testid="stMetric"] { min-height: 96px; }
          button[data-baseweb="tab"] {
            font-size: .64rem;
            padding-left: .68rem !important;
            padding-right: .68rem !important;
          }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str = "") -> None:
    sub_html = f'<div class="erp-sub">{subtitle}</div>' if subtitle else ""
    st.markdown(
        f"""
        <div class="erp-hero">
          <div class="srj-eyebrow">SHUBHRAJ JEWELS · ERP</div>
          <div class="erp-title">{title}</div>
          {sub_html}
        </div>
        """,
        unsafe_allow_html=True,
    )
