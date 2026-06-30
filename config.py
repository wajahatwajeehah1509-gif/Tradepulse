# config.py

# Page Configuration
PAGE_CONFIG = {
    "page_title": "TradePulse Dashboard",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "page_icon": "📉"
}

# Tickers for yfinance
TICKERS = {
    "Gold": "GC=F",
    "Oil": "CL=F",
    "USD/INR": "INR=X"
}

# Refresh interval in seconds (used for caching)
REFRESH_INTERVAL = 60
CACHE_TTL = 60
