import streamlit as st
from utils.formatting import format_currency

def render_metrics(market_data):
    """
    Renders the row of key metrics (Gold, Oil, USD/INR).
    """
    cols = st.columns(len(market_data))
    
    for col, (name, data) in zip(cols, market_data.items()):
        with col:
            if data:
                # Formatting logic
                currency_symbol = "₹" if name == "USD/INR" else "$"
                
                st.metric(
                    label=name,
                    value=format_currency(data['current_price'], currency_symbol),
                    delta=f"{data['change']:.2f} ({data['pct_change']:.2f}%)"
                )
            else:
                st.error(f"No data for {name}")
