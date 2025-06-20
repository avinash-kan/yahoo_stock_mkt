# Yahoo Stock Market ETL

This repository provides a simple ETL pipeline to collect fundamental and technical data for the Nifty 50 companies listed on the National Stock Exchange (NSE) of India using Yahoo Finance.

## Features

- **Fundamentals**: market capitalization, valuation ratios, beta, dividend yield and other key metrics.
- **Technicals**: 50-day and 200-day moving averages computed from the last year of daily closing prices.

## Usage

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Run the ETL script:

```bash
python main.py
```

The collected data will be saved to `data/nifty50_fundamentals.csv`.

## Requirements

- Python 3.8+
- `pandas`
- `yfinance`

