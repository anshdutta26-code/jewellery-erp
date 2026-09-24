import streamlit as st


def inject_css() -> None:
    st.markdown(
        """
        <style>
        .block-container {padding-top: 1.3rem; padding-bottom: 3rem; max-width: 1450px;}
        [data-testid="stSidebar"] {border-right: 1px solid rgba(128,128,128,.16);}
        div[data-testid="stMetric"] {border: 1px solid rgba(128,128,128,.18); border-radius: 12px; padding: 12px 14px;}
        .erp-title {font-size: 1.85rem; font-weight: 760; letter-spacing: -0.02em; margin-bottom: .15rem;}
        .erp-sub {opacity: .66; font-size: .92rem; margin-bottom: 1rem;}
        .voucher-box {border: 1px solid rgba(128,128,128,.22); padding: 14px; border-radius: 12px;}
        .muted {opacity:.68;}
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(title: str, subtitle: str = "") -> None:
    st.markdown(f'<div class="erp-title">{title}</div>', unsafe_allow_html=True)
    if subtitle:
        st.markdown(f'<div class="erp-sub">{subtitle}</div>', unsafe_allow_html=True)
