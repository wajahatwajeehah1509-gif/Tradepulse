import streamlit as st
import config

# Must be the first Streamlit command
st.set_page_config(**config.PAGE_CONFIG)

from services.market_data import MarketDataService
from components.sidebar import render_sidebar
from components.metrics import render_metrics
from components.charts import render_charts

def main():
    # Render Sidebar
    render_sidebar()

    # Main Header
    st.title("TradePulse 📉")
    st.markdown("### Real-time Market Data for IIFT Analysts")
    st.markdown("---")

    # Fetch Data
    with st.spinner('Fetching latest market data...'):
        market_data = MarketDataService.get_all_summaries()

    # Render Components
    render_metrics(market_data)
    
    st.markdown("---")
    
    render_charts(market_data)

if __name__ == "__main__":
    main()
