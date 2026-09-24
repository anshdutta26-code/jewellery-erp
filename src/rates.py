from __future__ import annotations

from datetime import datetime
from html import unescape
import re
from typing import Any
from zoneinfo import ZoneInfo

import requests
import streamlit as st


TROY_OUNCE_GRAMS = 31.1034768
INDIA_TZ = ZoneInfo("Asia/Kolkata")


def _get_json(url: str, timeout: int = 8) -> dict[str, Any]:
    response = requests.get(
        url,
        timeout=timeout,
        headers={"User-Agent": "Shubhraj-Jewels-ERP/1.0"},
    )
    response.raise_for_status()
    return response.json()


def _usd_inr() -> float:
    # Primary: open.er-api (free, no key). Fallback: Frankfurter.
    try:
        data = _get_json("https://open.er-api.com/v6/latest/USD")
        rate = float(data["rates"]["INR"])
        if rate > 0:
            return rate
    except Exception:
        pass

    data = _get_json("https://api.frankfurter.app/latest?from=USD&to=INR")
    return float(data["rates"]["INR"])


def _metal_usd_oz(symbol: str) -> float:
    data = _get_json(f"https://api.gold-api.com/price/{symbol}")
    for key in ("price", "ask", "close"):
        if key in data and data[key] is not None:
            return float(data[key])
    raise RuntimeError(f"No price returned for {symbol}")


def _diamond_india_1ct() -> tuple[float | None, str]:
    """
    Returns the current India-market average for a 1 carat natural diamond.
    Diamonds do not have a single spot rate, so this is explicitly a benchmark.
    """
    url = "https://jewelleryindia.in/diamond-prices/natural/1-carat/"
    try:
        response = requests.get(
            url,
            timeout=8,
            headers={
                "User-Agent": (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 Chrome/140 Safari/537.36"
                )
            },
        )
        response.raise_for_status()
        text = unescape(response.text)
        patterns = [
            r"current price for a 1 carat natural diamond in India is\s*₹\s*([\d,]+(?:\.\d+)?)",
            r"1 Carat Natural Diamond Prices.*?₹\s*([\d,]+(?:\.\d+)?)",
        ]
        for pattern in patterns:
            match = re.search(pattern, text, flags=re.I | re.S)
            if match:
                return float(match.group(1).replace(",", "")), "Jewellery India"
    except Exception:
        pass

    # Last-known benchmark at build time (24 Sep 2026). Clearly labelled in UI.
    return 336481.09, "Jewellery India · fallback 24 Sep 2026"


@st.cache_data(ttl=600, show_spinner=False)
def india_market_rates() -> dict[str, Any]:
    result: dict[str, Any] = {
        "gold_24k": None,
        "gold_22k": None,
        "silver_999": None,
        "diamond_1ct": None,
        "updated_at": datetime.now(INDIA_TZ),
        "metal_source": "Gold API + FX conversion",
        "diamond_source": "Jewellery India",
        "status": "live",
    }

    try:
        fx = _usd_inr()
        gold_usd_oz = _metal_usd_oz("XAU")
        silver_usd_oz = _metal_usd_oz("XAG")

        gold_24 = gold_usd_oz * fx / TROY_OUNCE_GRAMS
        silver_999 = silver_usd_oz * fx / TROY_OUNCE_GRAMS

        result["gold_24k"] = round(gold_24, 2)
        result["gold_22k"] = round(gold_24 * 22 / 24, 2)
        result["silver_999"] = round(silver_999, 2)
        result["usd_inr"] = round(fx, 4)
    except Exception as exc:
        result["status"] = "partial"
        result["metal_error"] = str(exc)

    diamond, source = _diamond_india_1ct()
    result["diamond_1ct"] = diamond
    result["diamond_source"] = source

    return result
