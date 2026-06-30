# TradePulse 📉

Real-time market data dashboard built for IIFT analysts, tracking key commodity and currency indicators with live charts and metrics.

## 🔗 Live Demo

**[View the live dashboard →](https://tradepulseworkshop-zcbg2mr7bjgdogg27qioet.streamlit.app/)**

## Overview

TradePulse is a Streamlit-based dashboard that pulls live market data via `yfinance` and presents it through clean, interactive visualizations — built for quick at-a-glance market monitoring.

## Features

- 📊 Real-time price metrics for tracked tickers
- 📈 Interactive charts powered by Plotly
- 🔄 Auto-refreshing data with configurable cache TTL
- 🧭 Sidebar navigation for easy access to controls
- ⚡ Wide-layout dashboard optimized for analysis

## Tracked Tickers

| Asset    | Ticker  |
|----------|---------|
| Gold     | GC=F    |
| Oil      | CL=F    |
| USD/INR  | INR=X   |

> Ticker list is configurable in `config.py` — add or remove instruments as needed.

## Tech Stack

- **Framework:** [Streamlit](https://streamlit.io/)
- **Data Source:** [yfinance](https://pypi.org/project/yfinance/)
- **Data Handling:** pandas
- **Visualization:** Plotly

## Project Structure

```
TradePulse/
├── app.py                      # Main application entry point
├── config.py                   # Page config, tickers, refresh settings
├── requirements.txt            # Python dependencies
├── services/
│   └── market_data.py          # Market data fetching service
└── components/
    ├── sidebar.py               # Sidebar UI component
    ├── metrics.py                # Metrics display component
    └── charts.py                 # Chart rendering component
```

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/<your-username>/TradePulse.git
   cd TradePulse
   ```

2. Create and activate a virtual environment (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the app locally with:

```bash
streamlit run app.py
```

The dashboard will open automatically in your default browser at `http://localhost:8501`.

## Configuration

Adjust the following in `config.py`:

- `TICKERS` — dictionary of asset names mapped to their yfinance ticker symbols
- `REFRESH_INTERVAL` / `CACHE_TTL` — control how frequently data is refreshed (in seconds)
- `PAGE_CONFIG` — Streamlit page title, layout, and icon settings

## Roadmap

- [ ] Add Silver and other precious metals
- [ ] Historical trend analysis
- [ ] Price alert notifications
- [ ] Export data to CSV/Excel

## License

This project is open source and available under the [MIT License](LICENSE).

---

Built with ❤️ using Streamlit.
