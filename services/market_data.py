import yfinance as yf
import pandas as pd
import streamlit as st
import config

class MarketDataService:
    @staticmethod
    @st.cache_data(ttl=config.CACHE_TTL)
    def fetch_data(ticker_symbol, period="1mo", interval="1d"):
        """
        Fetches historical data and current info for a ticker.
        Cached to prevent excessive API calls.
        """
        try:
            ticker = yf.Ticker(ticker_symbol)
            hist = ticker.history(period=period, interval=interval)
            info = ticker.info
            return hist, info
        except Exception as e:
            st.error(f"Error fetching data for {ticker_symbol}: {e}")
            return pd.DataFrame(), {}

    @classmethod
    def get_summary(cls, ticker_name):
        """
        Returns a summary dictionary for a given ticker name defined in config.
        """
        symbol = config.TICKERS.get(ticker_name)
        if not symbol:
            return None

        hist, info = cls.fetch_data(symbol)
        
        # Determine current price
        # Try different fields for current price as yfinance can be inconsistent across asset classes
        current_price = info.get('regularMarketPrice') or info.get('currentPrice') or info.get('previousClose')
        
        if current_price is None and not hist.empty:
            current_price = hist['Close'].iloc[-1]

        # Determine previous close for change calculation
        previous_close = info.get('previousClose')
        if previous_close is None and len(hist) > 1:
            previous_close = hist['Close'].iloc[-2]

        change = 0.0
        pct_change = 0.0

        if current_price and previous_close:
            change = current_price - previous_close
            pct_change = (change / previous_close) * 100

        return {
            'name': ticker_name,
            'current_price': current_price,
            'change': change,
            'pct_change': pct_change,
            'history': hist
        }

    @classmethod
    def get_all_summaries(cls):
        """
        Returns summaries for all tickers in config.
        """
        return {name: cls.get_summary(name) for name in config.TICKERS}
