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

        html, body, .stApp {
          font-family: "Montserrat", sans-serif;
        }

        .stApp input,
        .stApp textarea,
        .stApp select,
        .stApp button,
        .stApp label,
        .stApp p,
        .stApp div {
          font-family: "Montserrat", sans-serif;
        }

        .stApp .erp-title,
        .stApp .headline,
        .stApp h1,
        .stApp h2,
        .stApp h3,
        .stApp .kpi-value,
        .stApp .rate-value,
        .stApp .section-title,
        .stApp .panel-heading strong,
        .stApp .sidebar-monogram,
        .stApp .sidebar-name,
        .stApp .srj-monogram,
        .stApp .srj-name {
          font-family: "Cormorant Garamond", Georgia, serif !important;
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

        /* Password visibility: keep a true eye control, never raw icon text. */
        [data-testid="stTextInput"] button {
          min-width: 42px !important;
          width: 42px !important;
          height: 42px !important;
          padding: 0 !important;
          border: 0 !important;
          background: transparent !important;
          box-shadow: none !important;
          color: transparent !important;
          position: relative !important;
        }

        [data-testid="stTextInput"] button span,
        [data-testid="stTextInput"] button div {
          font-size: 0 !important;
          color: transparent !important;
        }

        [data-testid="stTextInput"] button::after {
          content: "👁";
          position: absolute;
          inset: 0;
          display: grid;
          place-items: center;
          color: #103C2B;
          font-size: 17px;
          line-height: 1;
        }

        /* Approved responsive dashboard */
        .dashboard-shell {
          width: 100%;
          padding-bottom: .5rem;
        }

        .dashboard-grid {
          display: grid;
          gap: 14px;
          margin-top: 14px;
        }

        .dashboard-grid-top {
          grid-template-columns: minmax(0, 1.65fr) minmax(280px, .85fr);
        }

        .dashboard-grid-bottom {
          grid-template-columns: minmax(0, 1.7fr) minmax(280px, .7fr);
          align-items: start;
        }

        .dashboard-panel {
          min-width: 0;
          border: 1px solid rgba(210,163,58,.28);
          border-radius: 12px;
          background: rgba(255,253,248,.94);
          padding: .95rem 1rem 1rem;
          box-shadow: 0 10px 28px rgba(10,46,34,.045);
        }

        .chart-shell {
          width: 100%;
          min-height: 245px;
          overflow: hidden;
          border-radius: 9px;
          background:
            linear-gradient(180deg, rgba(255,253,248,.96), rgba(248,243,232,.72));
          border: 1px solid rgba(210,163,58,.14);
        }

        .sales-svg {
          width: 100%;
          height: 245px;
          display: block;
        }

        .svg-grid {
          stroke: rgba(16,60,43,.09);
          stroke-width: 1;
          stroke-dasharray: 4 6;
        }

        .svg-line {
          fill: none;
          stroke: #D2A33A;
          stroke-width: 3;
          stroke-linecap: round;
          stroke-linejoin: round;
        }

        .svg-dot {
          fill: #103C2B;
          stroke: #E6C66E;
          stroke-width: 2;
        }

        .svg-axis {
          fill: #748278;
          font-size: 11px;
          font-family: "Montserrat", sans-serif;
        }

        .mix-wrap {
          min-height: 245px;
          display: grid;
          grid-template-columns: 160px minmax(0, 1fr);
          align-items: center;
          gap: 1rem;
          padding: .5rem;
        }

        .mix-donut {
          width: 154px;
          height: 154px;
          border-radius: 50%;
          display: grid;
          place-items: center;
          box-shadow: 0 8px 24px rgba(10,46,34,.06);
        }

        .mix-hole {
          width: 88px;
          height: 88px;
          border-radius: 50%;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          background: #FFFDF8;
          box-shadow: inset 0 0 0 1px rgba(210,163,58,.18);
        }

        .mix-hole span {
          color: #A67E29;
          font-size: .52rem;
          letter-spacing: .16em;
          font-weight: 700;
        }

        .mix-hole strong {
          margin-top: .12rem;
          font-family: "Cormorant Garamond", Georgia, serif !important;
          color: #0A2E22;
          font-size: 1.8rem;
          line-height: .9;
        }

        .mix-hole em {
          color: #7C887F;
          font-size: .48rem;
          font-style: normal;
          margin-top: .18rem;
        }

        .mix-legend {
          display: flex;
          flex-direction: column;
          gap: .48rem;
          min-width: 0;
        }

        .mix-legend-row {
          display: grid;
          grid-template-columns: 9px minmax(0, 1fr) auto;
          align-items: center;
          gap: .5rem;
          color: #53675A;
          font-size: .66rem;
        }

        .mix-swatch {
          width: 9px;
          height: 9px;
          border-radius: 50%;
        }

        .mix-legend-row strong {
          color: #0A2E22;
          font-size: .63rem;
        }

        .lux-table-wrap {
          overflow-x: auto;
          border: 1px solid rgba(210,163,58,.16);
          border-radius: 9px;
        }

        .lux-table {
          width: 100%;
          border-collapse: collapse;
          min-width: 680px;
          background: rgba(255,253,248,.78);
        }

        .lux-table th {
          text-align: left;
          padding: .66rem .72rem;
          background: rgba(16,60,43,.045);
          color: #708076;
          font-size: .52rem;
          letter-spacing: .11em;
          text-transform: uppercase;
          font-weight: 700;
          border-bottom: 1px solid rgba(210,163,58,.17);
        }

        .lux-table td {
          padding: .7rem .72rem;
          color: #42594A;
          font-size: .64rem;
          border-bottom: 1px solid rgba(16,60,43,.06);
          vertical-align: middle;
        }

        .lux-table tr:last-child td { border-bottom: 0; }

        .amount-cell {
          color: #0A2E22 !important;
          font-weight: 700;
          white-space: nowrap;
        }

        .voucher-chip,
        .status-chip {
          display: inline-flex;
          align-items: center;
          padding: .24rem .42rem;
          border-radius: 999px;
          font-size: .51rem;
          font-weight: 700;
          letter-spacing: .06em;
          white-space: nowrap;
        }

        .voucher-chip {
          color: #85651F;
          background: rgba(210,163,58,.11);
          border: 1px solid rgba(210,163,58,.20);
        }

        .status-chip {
          color: #246845;
          background: rgba(45,140,91,.09);
          border: 1px solid rgba(45,140,91,.17);
        }

        .empty-cell {
          text-align: center;
          color: #839087 !important;
          padding: 1.4rem !important;
        }

        .compact-empty {
          min-height: 245px;
        }

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
        [data-testid="stToolbar"] { display: none !important; }
        [data-testid="stHeader"] {
          background: transparent !important;
          box-shadow: none !important;
        }
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
          .dashboard-grid-top,
          .dashboard-grid-bottom {
            grid-template-columns: minmax(0, 1.3fr) minmax(260px, .8fr);
          }
        }

        @media (max-width: 900px) {
          [data-testid="stSidebar"] {
            width: min(82vw, 320px) !important;
            min-width: min(82vw, 320px) !important;
          }
          .kpi-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
          .kpi-card { min-height: 116px; }
          .kpi-value { font-size: 1.75rem; }
          .dashboard-grid-top,
          .dashboard-grid-bottom {
            grid-template-columns: 1fr;
          }
          .mix-wrap {
            grid-template-columns: 180px minmax(0, 1fr);
          }
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
          .dashboard-panel { padding: .78rem; }
          .chart-shell,
          .sales-svg,
          .compact-empty { min-height: 205px; height: 205px; }
          .mix-wrap {
            min-height: 205px;
            grid-template-columns: 132px minmax(0, 1fr);
            gap: .7rem;
            padding: .3rem;
          }
          .mix-donut { width: 126px; height: 126px; }
          .mix-hole { width: 72px; height: 72px; }
          .mix-hole strong { font-size: 1.45rem; }
          div[data-testid="stMetric"] { min-height: 96px; }
        }

        @media (max-width: 620px) {
          .mix-wrap {
            grid-template-columns: 1fr;
            justify-items: center;
          }
          .mix-legend { width: 100%; }
          .dashboard-panel { border-radius: 10px; }
          .lux-table { min-width: 620px; }
        }

        @media (max-width: 480px) {
          .rate-grid { grid-template-columns: 1fr 1fr; }
          .rate-card {
            min-height: 98px;
            padding: .66rem .58rem;
            gap: .48rem;
          }
          .rate-card .rate-icon {
            width: 34px;
            height: 34px;
            flex-basis: 34px;
          }
          .rate-label { font-size: .53rem; letter-spacing: .08em; }
          .rate-value { font-size: .94rem; }
          .rate-note { font-size: .46rem; line-height: 1.25; }
          .kpi-grid { grid-template-columns: 1fr 1fr; }
          .kpi-card:last-child { grid-column: span 2; }
          .section-title { font-size: 1.48rem; }
          .rate-disclaimer { font-size: .54rem; }
        }

        /* ===== Shubhraj approved dashboard / website-responsive shell ===== */
        .block-container {
          max-width: 1680px !important;
          padding-top: 1.05rem !important;
          padding-left: 1.15rem !important;
          padding-right: 1.15rem !important;
        }

        [data-testid="stSidebar"] {
          width: 232px !important;
          min-width: 232px !important;
          background:
            radial-gradient(circle at 20% 92%, rgba(198,155,60,.10), transparent 14rem),
            linear-gradient(180deg, #123C2C 0%, #0A2E22 100%) !important;
          border-right: 1px solid rgba(210,163,58,.42) !important;
        }

        [data-testid="stSidebar"] [data-testid="stSidebarContent"] {
          padding: .55rem .65rem .75rem !important;
        }

        .sidebar-brand {
          text-align: center;
          padding: .85rem .35rem 1.15rem !important;
          margin: 0 0 .4rem 0 !important;
          border-bottom: 1px solid rgba(230,198,110,.20);
        }

        .sidebar-brand::before { display: none !important; }
        .sidebar-monogram { display: none !important; }

        .sidebar-name {
          color: #F2E3B4 !important;
          font-family: "Cormorant Garamond", Georgia, serif !important;
          font-size: 1.75rem !important;
          font-weight: 600 !important;
          letter-spacing: .13em !important;
          line-height: .92 !important;
        }

        .sidebar-jewels {
          color: #E6C66E !important;
          font-family: "Cormorant Garamond", Georgia, serif !important;
          font-size: .95rem !important;
          letter-spacing: .26em !important;
          margin-top: .22rem !important;
        }

        .sidebar-tag {
          margin-top: .7rem;
          color: rgba(248,232,179,.58);
          font-size: .48rem;
          letter-spacing: .21em;
          line-height: 1.7;
        }

        [data-testid="stSidebar"] .stButton {
          margin: .08rem 0 !important;
        }

        [data-testid="stSidebar"] .stButton > button {
          width: 100% !important;
          min-height: 40px !important;
          justify-content: flex-start !important;
          gap: .55rem !important;
          padding: .48rem .66rem !important;
          border-radius: 7px !important;
          border: 1px solid transparent !important;
          background: transparent !important;
          color: rgba(255,248,230,.83) !important;
          box-shadow: none !important;
          font-size: .72rem !important;
          letter-spacing: .01em !important;
          text-transform: none !important;
          font-weight: 500 !important;
        }

        [data-testid="stSidebar"] .stButton > button:hover {
          background: rgba(230,198,110,.075) !important;
          border-color: rgba(230,198,110,.18) !important;
          color: #F8E8B3 !important;
        }

        [data-testid="stSidebar"] .stButton > button[kind="primary"],
        [data-testid="stSidebar"] .stButton > button[data-testid="stBaseButton-primary"] {
          background: linear-gradient(90deg, rgba(198,155,60,.23), rgba(198,155,60,.11)) !important;
          border: 1px solid rgba(230,198,110,.34) !important;
          color: #FFF3CE !important;
          box-shadow: inset 3px 0 0 #D2A33A !important;
        }

        [data-testid="stSidebar"] .stButton > button svg {
          color: #E6C66E !important;
          fill: #E6C66E !important;
          width: 18px !important;
          height: 18px !important;
        }

        .sidebar-legacy {
          margin: 1.05rem .2rem .85rem;
          min-height: 152px;
          display: flex;
          flex-direction: column;
          justify-content: center;
          align-items: center;
          text-align: center;
          border-radius: 78px 78px 0 0;
          border: 1px solid rgba(210,163,58,.25);
          background:
            radial-gradient(circle at 50% 0%, rgba(210,163,58,.12), transparent 7rem),
            rgba(5,31,23,.25);
        }

        .sidebar-legacy-mark {
          color: #D2A33A;
          font-size: 1.4rem;
          margin-bottom: .42rem;
        }

        .sidebar-legacy strong {
          color: #E7D7A8;
          font-family: "Cormorant Garamond", Georgia, serif !important;
          font-size: .77rem;
          letter-spacing: .16em;
          line-height: 1.25;
        }

        .sidebar-legacy span {
          margin-top: .4rem;
          color: rgba(248,232,179,.55);
          font-size: .46rem;
          letter-spacing: .22em;
        }

        /* Executive top header */
        .executive-topbar {
          display: grid;
          grid-template-columns: minmax(190px,.8fr) minmax(250px,1.2fr) minmax(360px,1.5fr);
          align-items: center;
          gap: 1.2rem;
          min-height: 76px;
          padding: .55rem .8rem .55rem .35rem;
          margin-bottom: .65rem;
          border-bottom: 1px solid rgba(126,92,44,.15);
          background: rgba(255,253,248,.76);
          backdrop-filter: blur(8px);
        }

        .greeting-title {
          color: #382417;
          font-family: "Cormorant Garamond", Georgia, serif !important;
          font-size: 1.85rem;
          font-weight: 700;
          line-height: .92;
        }

        .greeting-sub {
          color: #725C48;
          font-size: .65rem;
          margin-top: .26rem;
          font-weight: 600;
        }

        .topbar-motto {
          display: flex;
          align-items: center;
          gap: .8rem;
          padding-left: 1rem;
          border-left: 1px solid rgba(147,113,64,.20);
        }

        .motto-mark {
          color: #B68A37;
          font-size: 2rem;
          line-height: 1;
        }

        .topbar-motto div {
          display: flex;
          flex-direction: column;
        }

        .topbar-motto strong {
          color: #7F6C5C;
          font-size: .52rem;
          letter-spacing: .22em;
        }

        .topbar-motto em {
          color: #9D8B7A;
          font-size: .42rem;
          letter-spacing: .22em;
          font-style: normal;
          margin-top: .2rem;
        }

        .topbar-actions {
          display: flex;
          justify-content: flex-end;
          align-items: center;
          gap: .62rem;
        }

        .dashboard-search {
          min-width: 260px;
          padding: .58rem .76rem;
          border-radius: 8px;
          border: 1px solid rgba(83,59,39,.15);
          background: rgba(255,253,248,.82);
          color: #96887B;
          font-size: .58rem;
          box-shadow: 0 5px 14px rgba(60,40,25,.035);
        }

        .dashboard-search span {
          color: #654D3A;
          font-size: .9rem;
          margin-right: .3rem;
        }

        .profile-orb {
          width: 38px;
          height: 38px;
          border-radius: 50%;
          display: grid;
          place-items: center;
          background: #3B2B1D;
          color: #EAD9A7;
          border: 1px solid rgba(210,163,58,.45);
          font-family: "Cormorant Garamond", Georgia, serif !important;
          font-size: .92rem;
          font-weight: 700;
        }

        .profile-copy {
          display: flex;
          flex-direction: column;
          min-width: 86px;
        }

        .profile-copy strong {
          color: #4B3827;
          font-size: .60rem;
        }

        .profile-copy span {
          color: #9A8A7B;
          font-size: .45rem;
          margin-top: .12rem;
        }

        /* Banner mirrors the approved concept while using the website palette */
        .brand-banner {
          position: relative;
          overflow: hidden;
          min-height: 126px;
          display: grid;
          grid-template-columns: 1fr 1.35fr .72fr .62fr;
          align-items: center;
          gap: .5rem;
          padding: .85rem 1.1rem;
          margin-bottom: .72rem;
          border-radius: 10px;
          border: 1px solid rgba(184,138,55,.25);
          background:
            radial-gradient(circle at 81% 48%, rgba(210,163,58,.18), transparent 11rem),
            linear-gradient(110deg, #F9F5EC 0%, #F3EADC 61%, #E8D7BF 100%);
          box-shadow: 0 8px 24px rgba(55,34,18,.045);
        }

        .brand-banner::before {
          content: "";
          position: absolute;
          inset: 0;
          opacity: .26;
          background:
            repeating-linear-gradient(45deg, transparent 0 62px, rgba(167,129,72,.08) 63px 64px);
          pointer-events: none;
        }

        .banner-copy, .banner-center, .banner-arch {
          position: relative;
          z-index: 1;
        }

        .banner-copy {
          display: flex;
          flex-direction: column;
          color: #6B513A;
          font-family: "Cormorant Garamond", Georgia, serif !important;
        }

        .banner-copy span {
          font-size: .64rem;
          letter-spacing: .22em;
        }

        .banner-copy strong {
          margin-top: .17rem;
          font-size: .69rem;
          letter-spacing: .23em;
          font-weight: 600;
        }

        .banner-copy.right {
          padding-left: .7rem;
          border-left: 1px solid rgba(130,90,50,.18);
        }

        .banner-center {
          text-align: center;
          display: flex;
          flex-direction: column;
          align-items: center;
        }

        .banner-mark {
          color: #AF8334;
          font-size: 1.55rem;
          line-height: 1;
        }

        .banner-center strong {
          color: #4E3727;
          font-family: "Cormorant Garamond", Georgia, serif !important;
          font-size: 1.05rem;
          letter-spacing: .20em;
          margin-top: .16rem;
        }

        .banner-center em {
          color: #A58B71;
          font-style: normal;
          font-size: .41rem;
          letter-spacing: .26em;
          margin-top: .15rem;
        }

        .banner-arch {
          height: 115px;
          align-self: end;
          display: grid;
          place-items: end center;
          border-radius: 70px 70px 0 0;
          border: 9px solid rgba(173,128,63,.28);
          border-bottom: 0;
          background:
            radial-gradient(circle at 50% 85%, rgba(255,255,255,.78), transparent 3rem),
            linear-gradient(180deg, rgba(102,70,43,.08), rgba(255,255,255,.35));
        }

        .jewel-display {
          margin-bottom: .78rem;
          color: #A97628;
          font-size: 2.1rem;
          text-shadow: 0 5px 14px rgba(156,103,35,.16);
        }

        /* Market matrix: exact requested units */
        .rate-matrix {
          display: grid;
          grid-template-columns: repeat(3, minmax(0,1fr)) auto;
          gap: 10px;
          align-items: stretch;
          margin: .45rem 0 .2rem;
        }

        .market-cell {
          min-width: 0;
          display: flex;
          align-items: center;
          gap: .68rem;
          padding: .68rem .78rem;
          min-height: 82px;
          border-radius: 9px;
          border: 1px solid rgba(171,127,52,.22);
          background: rgba(255,253,248,.90);
          box-shadow: 0 6px 18px rgba(44,29,18,.035);
        }

        .market-symbol {
          width: 38px;
          height: 38px;
          flex: 0 0 38px;
          display: grid;
          place-items: center;
          border-radius: 50%;
          color: #E8D494;
          background: #113B2B;
          border: 1px solid rgba(205,161,68,.45);
          font-family: "Cormorant Garamond", Georgia, serif !important;
          font-weight: 700;
        }

        .diamond-cell .market-symbol {
          background: #F9F6F0;
          color: #6D5846;
        }

        .silver-cell .market-symbol {
          background: #E7E8E4;
          color: #505A55;
          border-color: #C9CEC8;
        }

        .market-copy {
          min-width: 0;
          display: flex;
          flex-direction: column;
        }

        .market-copy span {
          color: #806F60;
          font-size: .50rem;
          letter-spacing: .13em;
          font-weight: 700;
        }

        .market-copy strong {
          color: #163C2D;
          font-family: "Cormorant Garamond", Georgia, serif !important;
          font-size: 1.35rem;
          line-height: 1;
          margin-top: .15rem;
          white-space: nowrap;
        }

        .market-copy strong small {
          color: #7C827D;
          font-family: "Montserrat", sans-serif !important;
          font-size: .52rem;
          font-weight: 600;
        }

        .market-copy em {
          color: #9B8D80;
          font-size: .48rem;
          font-style: normal;
          margin-top: .18rem;
          line-height: 1.25;
        }

        .market-updated {
          min-width: 120px;
          display: flex;
          align-items: center;
          justify-content: center;
          gap: .38rem;
          color: #7A857E;
          font-size: .48rem;
          letter-spacing: .04em;
          border-radius: 9px;
          border: 1px solid rgba(21,58,44,.10);
          background: rgba(255,253,248,.56);
        }

        .market-updated span {
          width: 6px;
          height: 6px;
          border-radius: 50%;
          background: #2C8558;
          box-shadow: 0 0 0 3px rgba(44,133,88,.09);
        }

        .market-footnote {
          margin: .25rem .1rem .65rem;
          color: #9A8E83;
          font-size: .46rem;
          line-height: 1.45;
        }

        /* KPI row matches approved compact cards */
        .executive-kpis {
          display: grid;
          grid-template-columns: repeat(5, minmax(0,1fr));
          gap: 10px;
          margin-bottom: .72rem;
        }

        .executive-kpi {
          position: relative;
          min-width: 0;
          min-height: 116px;
          display: grid;
          grid-template-columns: 28px minmax(0,1fr);
          align-items: start;
          gap: .52rem;
          overflow: hidden;
          padding: .78rem .75rem;
          border-radius: 9px;
          border: 1px solid rgba(170,127,56,.23);
          background: rgba(255,253,248,.94);
          box-shadow: 0 7px 20px rgba(49,31,18,.04);
        }

        .kpi-glyph {
          width: 25px;
          height: 25px;
          display: grid;
          place-items: center;
          border-radius: 6px;
          color: #A57A2D;
          background: #F5EDDC;
          font-size: .78rem;
        }

        .executive-kpi > div:nth-child(2) {
          min-width: 0;
          display: flex;
          flex-direction: column;
        }

        .executive-kpi span {
          color: #61564C;
          font-size: .51rem;
          font-weight: 700;
          letter-spacing: .06em;
        }

        .executive-kpi strong {
          color: #2F231A;
          font-family: "Cormorant Garamond", Georgia, serif !important;
          font-size: 1.55rem;
          line-height: .95;
          margin-top: .28rem;
          white-space: nowrap;
        }

        .executive-kpi strong small {
          color: #655B52;
          font-family: "Montserrat", sans-serif !important;
          font-size: .58rem;
          font-weight: 600;
        }

        .executive-kpi em {
          color: #95877B;
          font-size: .48rem;
          font-style: normal;
          margin-top: .34rem;
        }

        .kpi-art {
          position: absolute;
          right: 9px;
          bottom: 8px;
          color: rgba(181,130,41,.32);
          font-family: Georgia, serif !important;
          font-size: 2.2rem;
          transform: rotate(-7deg);
        }

        .ring-art { font-size: 2.5rem; color: rgba(108,118,120,.25); }
        .bars-art { color: rgba(180,126,34,.34); }
        .bangle-art { font-size: 3rem; color: rgba(181,130,41,.30); }

        /* Analytics row mirrors approved 3-column composition */
        .analytics-three {
          display: grid;
          grid-template-columns: minmax(0, 1.8fr) minmax(260px, .8fr) minmax(260px, .78fr);
          gap: 10px;
          margin-bottom: 10px;
        }

        .dashboard-panel {
          border-radius: 9px !important;
          border: 1px solid rgba(170,127,56,.22) !important;
          background: rgba(255,253,248,.93) !important;
          box-shadow: 0 7px 20px rgba(49,31,18,.035) !important;
          padding: .72rem .75rem !important;
        }

        .panel-heading {
          margin: 0 0 .5rem !important;
        }

        .panel-heading span {
          display: none;
        }

        .panel-heading strong {
          color: #453224 !important;
          font-size: 1.02rem !important;
        }

        .panel-heading em {
          align-self: center;
          padding: .24rem .4rem;
          border-radius: 5px;
          border: 1px solid rgba(93,65,42,.13);
          background: #FAF7F0;
          color: #8A7B6F !important;
          font-size: .43rem !important;
        }

        .chart-shell {
          min-height: 238px !important;
          height: 238px !important;
          border-color: rgba(168,126,58,.11) !important;
        }

        .sales-svg {
          height: 238px !important;
        }

        .svg-bar {
          fill: rgba(205,157,62,.18);
        }

        .svg-line {
          stroke: #B98A31 !important;
          stroke-width: 2.2 !important;
        }

        .svg-dot {
          fill: #B98A31 !important;
          stroke: #FFF7DF !important;
          stroke-width: 1.5 !important;
        }

        .mix-wrap {
          min-height: 238px !important;
          grid-template-columns: 145px minmax(0,1fr) !important;
          gap: .7rem !important;
        }

        .mix-donut {
          width: 140px !important;
          height: 140px !important;
        }

        .mix-hole {
          width: 80px !important;
          height: 80px !important;
        }

        .mix-hole span {
          font-size: .42rem !important;
          letter-spacing: .08em !important;
        }

        .mix-hole strong {
          font-size: .82rem !important;
          text-align: center;
          max-width: 70px;
        }

        .stock-watch-list {
          display: flex;
          flex-direction: column;
          gap: .28rem;
        }

        .stock-watch-row {
          display: grid;
          grid-template-columns: 28px minmax(0,1fr) auto;
          align-items: center;
          gap: .5rem;
          padding: .38rem .3rem;
          border-bottom: 1px solid rgba(91,68,49,.07);
        }

        .watch-jewel {
          width: 27px;
          height: 27px;
          display: grid;
          place-items: center;
          border-radius: 7px;
          background: #F2EADC;
          color: #AB7C2A;
          font-size: .9rem;
        }

        .stock-watch-row > div:nth-child(2) {
          min-width: 0;
          display: flex;
          flex-direction: column;
        }

        .stock-watch-row strong {
          color: #4B382A;
          font-size: .55rem;
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;
        }

        .stock-watch-row em {
          color: #A19387;
          font-size: .42rem;
          font-style: normal;
          margin-top: .1rem;
        }

        .watch-count {
          color: #B14E4C;
          font-size: .52rem;
          text-align: right;
          white-space: nowrap;
        }

        .watch-count small {
          display: block;
          margin-top: .12rem;
          padding: .10rem .22rem;
          border-radius: 3px;
          background: rgba(183,72,70,.08);
          font-size: .36rem;
        }

        .stock-watch-empty {
          min-height: 180px;
          display: grid;
          place-items: center;
          color: #8C8177;
          font-size: .58rem;
          text-align: center;
        }

        .dashboard-bottom-row {
          display: grid;
          grid-template-columns: minmax(0, 3.2fr) minmax(230px, .8fr);
          gap: 10px;
          align-items: stretch;
        }

        .legacy-card {
          min-height: 180px;
          display: flex;
          flex-direction: column;
          justify-content: center;
          padding: 1rem 1.05rem;
          border-radius: 9px;
          border: 1px solid rgba(165,119,48,.26);
          background:
            radial-gradient(circle at 90% 75%, rgba(177,129,55,.16), transparent 7rem),
            linear-gradient(135deg, #F6EFE3, #E7D6BE);
          color: #74573E;
          overflow: hidden;
          position: relative;
        }

        .legacy-card::after {
          content: "";
          position: absolute;
          right: -35px;
          bottom: -55px;
          width: 120px;
          height: 170px;
          border: 13px solid rgba(145,101,47,.22);
          border-radius: 60px 60px 0 0;
        }

        .legacy-card span {
          font-size: .50rem;
          letter-spacing: .18em;
        }

        .legacy-card strong {
          margin-top: .16rem;
          font-family: "Cormorant Garamond", Georgia, serif !important;
          font-size: .82rem;
          letter-spacing: .16em;
        }

        .legacy-line {
          width: 28px;
          height: 1px;
          margin: .6rem 0;
          background: #B58835;
        }

        .legacy-mark {
          color: #A7782C;
          font-size: 1.35rem;
        }

        .legacy-card em {
          margin-top: .28rem;
          color: #6E5139;
          font-family: "Cormorant Garamond", Georgia, serif !important;
          font-style: normal;
          font-size: .58rem;
          letter-spacing: .15em;
        }

        .lux-table th {
          background: #F2EEE7 !important;
          color: #766B61 !important;
          font-size: .44rem !important;
        }

        .lux-table td {
          color: #55483E !important;
          font-size: .51rem !important;
          padding: .48rem .55rem !important;
        }

        .status-chip {
          color: #397B51 !important;
          background: rgba(64,145,91,.08) !important;
        }

        /* True CSS eye icon: no 'visibility' text and no emoji */
        [data-testid="stTextInput"] button::before {
          content: "";
          position: absolute;
          width: 16px;
          height: 10px;
          left: 13px;
          top: 15px;
          border: 1.8px solid #103C2B;
          border-radius: 50% / 58%;
          transform: rotate(-2deg);
        }

        [data-testid="stTextInput"] button::after {
          content: "";
          position: absolute;
          width: 4px;
          height: 4px;
          left: 19px;
          top: 18px;
          border-radius: 50%;
          background: #103C2B;
        }

        /* Mobile website-style hamburger: three lines on the right */
        @media (max-width: 900px) {
          .block-container {
            padding-top: 4.8rem !important;
            padding-left: .78rem !important;
            padding-right: .78rem !important;
          }

          [data-testid="stHeader"] {
            display: block !important;
            height: 64px !important;
            background: rgba(255,253,248,.96) !important;
            border-bottom: 1px solid rgba(187,143,61,.14) !important;
          }

          [data-testid="stHeader"]::before {
            content: "SHUBHRAJ  JEWELS";
            position: fixed;
            left: 18px;
            top: 21px;
            z-index: 1000000;
            color: #B78A35;
            font-family: "Cormorant Garamond", Georgia, serif;
            font-size: 1rem;
            font-weight: 700;
            letter-spacing: .12em;
          }

          [data-testid="stSidebarCollapsedControl"],
          [data-testid="collapsedControl"] {
            position: fixed !important;
            top: 12px !important;
            right: 14px !important;
            left: auto !important;
            z-index: 1000002 !important;
            width: 44px !important;
            height: 44px !important;
          }

          [data-testid="stSidebarCollapsedControl"] button,
          [data-testid="collapsedControl"] button,
          [data-testid="stSidebarCollapsedControl"],
          [data-testid="collapsedControl"] {
            border: 0 !important;
            border-radius: 7px !important;
            background: #123C2C !important;
            box-shadow: 0 5px 15px rgba(10,46,34,.13) !important;
          }

          [data-testid="stSidebarCollapsedControl"] svg,
          [data-testid="stSidebarCollapsedControl"] span,
          [data-testid="collapsedControl"] svg,
          [data-testid="collapsedControl"] span {
            display: none !important;
          }

          [data-testid="stSidebarCollapsedControl"]::before,
          [data-testid="collapsedControl"]::before {
            content: "";
            position: absolute;
            width: 21px;
            height: 14px;
            left: 11px;
            top: 14px;
            background:
              linear-gradient(#E8CC7A,#E8CC7A) 0 0/21px 2px no-repeat,
              linear-gradient(#E8CC7A,#E8CC7A) 0 6px/21px 2px no-repeat,
              linear-gradient(#E8CC7A,#E8CC7A) 0 12px/21px 2px no-repeat;
          }

          [data-testid="stSidebar"] {
            width: min(86vw, 340px) !important;
            min-width: min(86vw, 340px) !important;
            z-index: 1000003 !important;
            box-shadow: 10px 0 32px rgba(4,25,18,.18) !important;
          }

          [data-testid="stSidebarHeader"] button,
          [data-testid="stSidebar"] [data-testid="stBaseButton-headerNoPadding"] {
            width: 40px !important;
            height: 40px !important;
            border-radius: 7px !important;
            background: rgba(230,198,110,.08) !important;
            color: transparent !important;
          }

          [data-testid="stSidebarHeader"] button svg,
          [data-testid="stSidebarHeader"] button span {
            display: none !important;
          }

          [data-testid="stSidebarHeader"] button::after {
            content: "×";
            color: #E8CC7A;
            font-size: 1.8rem;
            line-height: 1;
          }

          .executive-topbar {
            display: none;
          }

          .brand-banner {
            min-height: 118px;
            grid-template-columns: 1fr;
            padding: .85rem;
          }

          .banner-copy,
          .banner-arch {
            display: none;
          }

          .banner-center strong {
            font-size: 1.12rem;
          }

          .banner-center em {
            font-size: .43rem;
          }

          .rate-matrix {
            grid-template-columns: 1fr;
            gap: 8px;
          }

          .market-cell {
            min-height: 74px;
          }

          .market-updated {
            min-height: 34px;
            order: -1;
          }

          .executive-kpis {
            grid-template-columns: repeat(2, minmax(0,1fr));
            gap: 8px;
          }

          .executive-kpi {
            min-height: 102px;
            padding: .66rem .64rem;
          }

          .executive-kpi:last-child {
            grid-column: span 2;
          }

          .executive-kpi strong {
            font-size: 1.32rem;
          }

          .analytics-three {
            grid-template-columns: 1fr;
            gap: 8px;
          }

          .dashboard-bottom-row {
            grid-template-columns: 1fr;
            gap: 8px;
          }

          .chart-shell,
          .sales-svg {
            height: 215px !important;
            min-height: 215px !important;
          }

          .mix-wrap {
            grid-template-columns: 130px minmax(0,1fr) !important;
            min-height: 190px !important;
          }

          .mix-donut {
            width: 124px !important;
            height: 124px !important;
          }

          .legacy-card {
            min-height: 145px;
          }
        }

        @media (min-width: 901px) and (max-width: 1180px) {
          .executive-topbar {
            grid-template-columns: 1fr 1fr;
          }
          .topbar-actions {
            grid-column: span 2;
            justify-content: flex-start;
          }
          .brand-banner {
            grid-template-columns: .8fr 1.2fr .6fr;
          }
          .banner-copy.right { display: none; }
          .rate-matrix {
            grid-template-columns: repeat(3, 1fr);
          }
          .market-updated {
            grid-column: span 3;
            min-height: 32px;
          }
          .executive-kpis {
            grid-template-columns: repeat(3,1fr);
          }
          .analytics-three {
            grid-template-columns: 1.6fr 1fr;
          }
          .stock-watch-panel {
            grid-column: span 2;
          }
        }


        .erp-footer {
          margin-top: .6rem;
          padding: .48rem .15rem .18rem;
          display: flex;
          align-items: center;
          justify-content: space-between;
          gap: 1rem;
          border-top: 1px solid rgba(139,102,55,.14);
          color: #8D8176;
          font-size: .44rem;
          letter-spacing: .03em;
        }

        .erp-footer > div {
          display: flex;
          align-items: center;
          gap: .45rem;
        }

        .erp-footer strong {
          color: #5B4939;
          font-size: .46rem;
          letter-spacing: .08em;
        }

        .erp-footer span {
          padding-left: .45rem;
          border-left: 1px solid rgba(120,91,55,.18);
        }

        .erp-footer b {
          color: #B48A3A;
          font-weight: 400;
        }

        @media (max-width: 900px) {
          [data-testid="stHeader"] button[kind="headerNoPadding"] {
            position: fixed !important;
            top: 12px !important;
            right: 14px !important;
            left: auto !important;
            z-index: 1000002 !important;
            width: 44px !important;
            height: 44px !important;
            border: 0 !important;
            border-radius: 7px !important;
            background: #123C2C !important;
            color: transparent !important;
            box-shadow: 0 5px 15px rgba(10,46,34,.13) !important;
          }

          [data-testid="stHeader"] button[kind="headerNoPadding"] svg,
          [data-testid="stHeader"] button[kind="headerNoPadding"] span {
            display: none !important;
          }

          [data-testid="stHeader"] button[kind="headerNoPadding"]::before {
            content: "";
            position: absolute;
            width: 21px;
            height: 14px;
            left: 11px;
            top: 14px;
            background:
              linear-gradient(#E8CC7A,#E8CC7A) 0 0/21px 2px no-repeat,
              linear-gradient(#E8CC7A,#E8CC7A) 0 6px/21px 2px no-repeat,
              linear-gradient(#E8CC7A,#E8CC7A) 0 12px/21px 2px no-repeat;
          }

          .erp-footer {
            flex-direction: column;
            align-items: flex-start;
            gap: .28rem;
            font-size: .42rem;
            padding-bottom: .8rem;
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
