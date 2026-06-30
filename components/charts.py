import streamlit as st
import plotly.express as px

def render_charts(market_data):
    """
    Renders the tabs and charts for historical data.
    """
    st.subheader("Price Trends (Last 30 Days)")
    
    ticker_names = list(market_data.keys())
    tabs = st.tabs(ticker_names)
    
    for tab, name in zip(tabs, ticker_names):
        with tab:
            data = market_data.get(name)
            if data and not data['history'].empty:
                hist_df = data['history']
                # Create Plotly figure
                fig = px.line(hist_df, y='Close', title=f"{name} Price History")
                
                # Customize layout
                fig.update_layout(
                    xaxis_title="Date",
                    yaxis_title="Price",
                    hovermode="x unified",
                    template="plotly_dark"  # Good for dashboards
                )
                
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No historical data available to chart.")
