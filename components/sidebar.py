import streamlit as st
import datetime

def render_sidebar():
    """
    Renders the sidebar content.
    """
    with st.sidebar:
        st.header("Settings")
        
        if st.button("Refresh Data", type="primary"):
            st.cache_data.clear()
            st.rerun()
            
        st.caption(f"Last updated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        st.markdown("---")
        st.markdown("### About")
        st.info(
            "This dashboard provides real-time market data for IIFT analysts. "
            "Data source: Yahoo Finance."
        )
