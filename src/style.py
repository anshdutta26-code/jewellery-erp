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
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,600&family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,300,0,0&family=Montserrat:wght@400;500;600;700&display=swap');

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
          background-color: #FBF6EB;
          background-image:
            repeating-linear-gradient(
              45deg,
              rgba(210,163,58,.045) 0px,
              rgba(210,163,58,.045) 1px,
              transparent 1px,
              transparent 52px
            ),
            repeating-linear-gradient(
              -45deg,
              rgba(16,60,43,.028) 0px,
              rgba(16,60,43,.028) 1px,
              transparent 1px,
              transparent 52px
            ),
            radial-gradient(circle at 12% 18%, rgba(210,163,58,.18), transparent 15rem),
            radial-gradient(circle at 88% 22%, rgba(16,60,43,.11), transparent 20rem),
            radial-gradient(circle at 82% 82%, rgba(210,163,58,.12), transparent 22rem),
            linear-gradient(180deg, #FFFDF9 0%, #F7F0E2 100%);
          background-attachment: fixed;
          color: var(--srj-green-dark);
        }

        .block-container {
          padding-top: 1.45rem;
          padding-bottom: 3rem;
          max-width: 1480px;
        }

        /* Header / titles */
        .erp-hero {
          margin: 0 0 1.15rem 0;
          padding: 1.2rem 1.35rem;
          border: 1px solid rgba(210,163,58,.48);
          border-radius: 10px;
          background: linear-gradient(135deg, #123E2C 0%, #0A2E22 100%);
          box-shadow: 0 10px 24px rgba(10,46,34,.08);
        }

        .erp-hero .srj-eyebrow { color: #E6C66E; }
        .erp-hero .erp-title { color: #FFF8E6; margin-bottom: .28rem; }
        .erp-hero .erp-sub { color: rgba(255,248,230,.72); margin-bottom: 0; }

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
          position: relative;
          overflow: hidden;
          background: rgba(255,253,248,.82);
          border: 1px solid rgba(210,163,58,.28);
          border-radius: 10px;
          padding: 1rem;
          box-shadow: 0 12px 28px rgba(10,46,34,.045);
          backdrop-filter: blur(3px);
        }

        .stApp [data-testid="stForm"]::before {
          content: "";
          position: absolute;
          width: 150px;
          height: 150px;
          right: -75px;
          bottom: -85px;
          border: 1px solid rgba(210,163,58,.12);
          border-radius: 50%;
          box-shadow:
            0 0 0 18px rgba(210,163,58,.035),
            0 0 0 36px rgba(16,60,43,.025);
          pointer-events: none;
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
          position: relative;
          text-align: center;
          max-width: 660px;
          margin: 0 auto .7rem auto;
          padding: .25rem 1rem .15rem 1rem;
        }

        .login-brand::before,
        .login-brand::after {
          position: absolute;
          font-family: "Cormorant Garamond", Georgia, serif;
          color: rgba(210,163,58,.28);
          line-height: 1;
          pointer-events: none;
        }

        .login-brand::before {
          content: "✦";
          left: 2%;
          top: 38%;
          font-size: 2.4rem;
        }

        .login-brand::after {
          content: "◇";
          right: 1%;
          top: 20%;
          font-size: 4.8rem;
          transform: rotate(12deg);
          color: rgba(16,60,43,.09);
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

        /* Restore Streamlit's Material icons after global font branding. */
        [data-testid="stIconMaterial"],
        .material-symbols-rounded,
        span[class*="material-symbols"] {
          font-family: "Material Symbols Rounded" !important;
          font-weight: normal !important;
          font-style: normal !important;
          letter-spacing: normal !important;
          text-transform: none !important;
          white-space: nowrap !important;
          word-wrap: normal !important;
          direction: ltr !important;
          -webkit-font-feature-settings: "liga" !important;
          -webkit-font-smoothing: antialiased !important;
        }

        /* Keep Streamlit chrome discreet; sidebar opener remains available. */
        [data-testid="stToolbar"] {
          opacity: .32;
          transition: opacity .18s ease;
        }
        [data-testid="stToolbar"]:hover { opacity: 1; }
        #MainMenu, footer { visibility: hidden; }

        /* Sidebar: luxury navigation, no default radio bullets. */
        [data-testid="stSidebar"] {
          width: 300px !important;
          min-width: 300px !important;
        }

        [data-testid="stSidebar"] [data-baseweb="radio"] > div:first-child {
          display: none !important;
        }

        [data-testid="stSidebar"] [role="radiogroup"] label {
          min-height: 42px;
          display: flex !important;
          align-items: center !important;
          padding: .56rem .78rem !important;
          margin: .08rem 0;
          border-radius: 7px !important;
          font-size: .88rem;
          letter-spacing: .01em;
        }

        [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
          background: linear-gradient(90deg, rgba(210,163,58,.18), rgba(210,163,58,.07)) !important;
          border: 1px solid rgba(230,198,110,.48) !important;
          box-shadow: inset 3px 0 0 #D2A33A !important;
        }

        .sidebar-brand {
          padding: .9rem .75rem .2rem;
          margin-bottom: .45rem;
        }

        .sidebar-monogram {
          font-size: 3.1rem;
          color: #E6C66E;
        }

        .sidebar-name {
          font-size: 1rem;
          line-height: 1.05;
          letter-spacing: .12em;
          color: #E6C66E;
        }

        .sidebar-jewels {
          margin-top: .28rem;
          font-size: .50rem;
          letter-spacing: .28em;
        }

        /* Approved dashboard composition */
        .market-head {
          display: flex;
          align-items: end;
          justify-content: space-between;
          gap: 1rem;
          margin: .2rem 0 .8rem;
        }

        .section-kicker {
          color: #B88A27;
          font-size: .65rem;
          letter-spacing: .22em;
          font-weight: 700;
          text-transform: uppercase;
          margin-bottom: .16rem;
        }

        .section-title {
          color: #0A2E22;
          font-family: "Cormorant Garamond", Georgia, serif;
          font-size: 1.72rem;
          line-height: 1;
          font-weight: 700;
        }

        .live-pill {
          flex: 0 0 auto;
          display: inline-flex;
          align-items: center;
          gap: .42rem;
          padding: .36rem .62rem;
          border: 1px solid rgba(16,60,43,.15);
          border-radius: 999px;
          background: rgba(255,253,248,.78);
          color: #6C7C6A;
          font-size: .62rem;
          letter-spacing: .045em;
          white-space: nowrap;
        }

        .live-pill span {
          width: 7px;
          height: 7px;
          border-radius: 50%;
          background: #2D8C5B;
          box-shadow: 0 0 0 4px rgba(45,140,91,.10);
        }

        .rate-grid {
          display: grid;
          grid-template-columns: repeat(4, minmax(0, 1fr));
          gap: 12px;
        }

        .rate-card {
          display: flex;
          align-items: center;
          gap: .85rem;
          min-height: 108px;
          padding: .9rem 1rem;
          border: 1px solid rgba(210,163,58,.30);
          border-radius: 12px;
          background:
            linear-gradient(145deg, rgba(255,253,248,.97), rgba(248,243,232,.87));
          box-shadow: 0 8px 22px rgba(10,46,34,.045);
        }

        .rate-card .rate-icon {
          display: grid;
          place-items: center;
          width: 46px;
          height: 46px;
          flex: 0 0 46px;
          border-radius: 50%;
          font-family: "Cormorant Garamond", Georgia, serif;
          font-size: 1.15rem;
          font-weight: 700;
          background: #103C2B;
          color: #E6C66E;
          border: 1px solid rgba(210,163,58,.55);
        }

        .rate-card.silver .rate-icon {
          background: #E7E9E5;
          color: #3D4B43;
          border-color: #C9CFC9;
        }

        .rate-card.diamond .rate-icon {
          background: #FFFDF8;
          color: #103C2B;
          border-color: rgba(16,60,43,.22);
          font-size: 1.55rem;
        }

        .rate-label {
          color: #6C7C6A;
          font-size: .61rem;
          font-weight: 700;
          letter-spacing: .12em;
          text-transform: uppercase;
        }

        .rate-value {
          margin-top: .18rem;
          color: #0A2E22;
          font-family: "Cormorant Garamond", Georgia, serif;
          font-size: 1.37rem;
          font-weight: 700;
          line-height: 1.05;
        }

        .rate-note {
          margin-top: .17rem;
          color: #849086;
          font-size: .59rem;
        }

        .rate-disclaimer {
          color: #829086;
          font-size: .58rem;
          line-height: 1.45;
          margin: .48rem 0 1.15rem;
        }

        .kpi-kicker { margin: .15rem 0 .55rem; }

        .kpi-grid {
          display: grid;
          grid-template-columns: repeat(5, minmax(0, 1fr));
          gap: 12px;
          margin-bottom: 1.35rem;
        }

        .kpi-card {
          position: relative;
          min-height: 128px;
          padding: .95rem 1rem;
          border: 1px solid rgba(210,163,58,.30);
          border-radius: 12px;
          overflow: hidden;
          background: rgba(255,253,248,.95);
          box-shadow: 0 8px 22px rgba(10,46,34,.045);
        }

        .kpi-card::after {
          content: "";
          position: absolute;
          width: 80px;
          height: 80px;
          right: -40px;
          top: -40px;
          border-radius: 50%;
          border: 1px solid rgba(210,163,58,.13);
          box-shadow: 0 0 0 14px rgba(210,163,58,.025);
        }

        .kpi-label {
          color: #6C7C6A;
          font-size: .61rem;
          letter-spacing: .14em;
          text-transform: uppercase;
          font-weight: 700;
        }

        .kpi-value {
          margin-top: .42rem;
          color: #0A2E22;
          font-family: "Cormorant Garamond", Georgia, serif;
          font-size: 2rem;
          font-weight: 700;
          line-height: .95;
        }

        .kpi-value span {
          font-family: "Montserrat", sans-serif;
          font-size: .78rem;
          font-weight: 600;
          color: #6C7C6A;
        }

        .kpi-meta {
          margin-top: .55rem;
          color: #8A948C;
          font-size: .58rem;
          line-height: 1.25;
        }

        .panel-heading {
          display: flex;
          align-items: end;
          justify-content: space-between;
          gap: 1rem;
          margin: .2rem 0 .6rem;
          padding: 0 .05rem;
        }

        .panel-heading div {
          display: flex;
          flex-direction: column;
        }

        .panel-heading span {
          color: #B88A27;
          font-size: .59rem;
          font-weight: 700;
          letter-spacing: .17em;
        }

        .panel-heading strong {
          color: #0A2E22;
          font-family: "Cormorant Garamond", Georgia, serif;
          font-size: 1.45rem;
          line-height: 1;
        }

        .panel-heading em {
          color: #88948C;
          font-style: normal;
          font-size: .58rem;
        }

        [data-testid="stVegaLiteChart"] {
          background: rgba(255,253,248,.92);
          border: 1px solid rgba(210,163,58,.24);
          border-radius: 12px;
          padding: .55rem;
          box-shadow: 0 8px 22px rgba(10,46,34,.04);
        }

        .empty-panel {
          display: grid;
          place-items: center;
          min-height: 275px;
          padding: 1rem;
          border-radius: 12px;
          border: 1px dashed rgba(210,163,58,.34);
          background: rgba(255,253,248,.72);
          color: #7E8A81;
          font-size: .78rem;
          text-align: center;
        }

        .table-title { margin-top: 1rem; }

        .attention-card {
          margin-top: 1rem;
          padding: 1rem;
          border-radius: 12px;
          background:
            radial-gradient(circle at 95% 0%, rgba(230,198,110,.10), transparent 8rem),
            linear-gradient(135deg, #123E2C 0%, #0A2E22 100%);
          color: #FFF8E6;
          border: 1px solid rgba(210,163,58,.52);
          box-shadow: 0 10px 24px rgba(10,46,34,.09);
        }

        .attention-top {
          display: flex;
          align-items: start;
          justify-content: space-between;
          gap: 1rem;
        }

        .attention-top div:first-child {
          display: flex;
          flex-direction: column;
        }

        .attention-top span {
          color: #E6C66E;
          font-size: .58rem;
          font-weight: 700;
          letter-spacing: .17em;
        }

        .attention-top strong {
          font-family: "Cormorant Garamond", Georgia, serif;
          font-size: 1.45rem;
          line-height: 1;
        }

        .attention-count {
          display: grid;
          place-items: center;
          width: 34px;
          height: 34px;
          border-radius: 50%;
          background: rgba(210,163,58,.14);
          border: 1px solid rgba(230,198,110,.42);
          color: #E6C66E;
          font-weight: 700;
        }

        .attention-card p {
          margin: .7rem 0 0;
          color: rgba(255,248,230,.64);
          font-size: .66rem;
          line-height: 1.45;
        }

        .attention-row {
          display: flex;
          align-items: center;
          justify-content: space-between;
          gap: .8rem;
          margin-top: .45rem;
          padding: .62rem .72rem;
          border-radius: 8px;
          border: 1px solid rgba(210,163,58,.23);
          background: rgba(255,253,248,.80);
          color: #496252;
          font-size: .64rem;
        }

        .attention-row strong {
          color: #0A2E22;
          white-space: nowrap;
        }

        .attention-row.ok strong { color: #2D8C5B; }

        @media (max-width: 1180px) {
          .rate-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
          .kpi-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); }
        }

        @media (max-width: 900px) {
          [data-testid="stSidebar"] {
            width: min(82vw, 320px) !important;
            min-width: min(82vw, 320px) !important;
          }
          .kpi-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
          .kpi-card { min-height: 116px; }
          .kpi-value { font-size: 1.75rem; }
        }

        @media (max-width: 800px) {
          .block-container {
            padding-top: 3.7rem;
            padding-left: .85rem;
            padding-right: .85rem;
          }
          .login-brand { padding-top: 1.2rem; }
          .erp-hero {
            padding: .95rem 1rem;
            margin-bottom: .85rem;
          }
          .erp-title { font-size: 1.92rem; }
          .erp-sub { font-size: .73rem; }
          .login-brand .headline { font-size: 2.1rem; }
          .market-head {
            align-items: start;
            flex-direction: column;
            gap: .45rem;
          }
          .rate-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 9px;
          }
          .rate-card {
            min-height: 104px;
            padding: .75rem .7rem;
            gap: .6rem;
          }
          .rate-card .rate-icon {
            width: 38px;
            height: 38px;
            flex-basis: 38px;
            font-size: 1rem;
          }
          .rate-value { font-size: 1.08rem; }
          .rate-note { font-size: .52rem; }
          .kpi-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 9px;
          }
          .kpi-card {
            min-height: 106px;
            padding: .78rem .75rem;
          }
          .kpi-value { font-size: 1.55rem; }
          .kpi-meta { font-size: .52rem; }
          .panel-heading strong { font-size: 1.25rem; }
          .panel-heading em { display: none; }
          div[data-testid="stMetric"] { min-height: 96px; }
        }

        @media (max-width: 480px) {
          .rate-grid { grid-template-columns: 1fr; }
          .kpi-grid { grid-template-columns: 1fr 1fr; }
          .kpi-card:last-child { grid-column: span 2; }
          .section-title { font-size: 1.48rem; }
          .rate-disclaimer { font-size: .54rem; }
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
