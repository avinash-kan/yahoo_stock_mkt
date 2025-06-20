import pandas as pd
import yfinance as yf

from .tickers import TICKERS


def fetch_fundamental_data(ticker: str) -> dict:
    """Return selected fundamental data for a ticker."""
    stock = yf.Ticker(ticker)
    info = stock.info
    return {
        "ticker": ticker,
        "shortName": info.get("shortName"),
        "sector": info.get("sector"),
        "marketCap": info.get("marketCap"),
        "trailingPE": info.get("trailingPE"),
        "forwardPE": info.get("forwardPE"),
        "priceToBook": info.get("priceToBook"),
        "beta": info.get("beta"),
        "dividendYield": info.get("dividendYield"),
        "profitMargins": info.get("profitMargins"),
    }


def fetch_technical_data(ticker: str) -> dict:
    """Calculate basic technical indicators for a ticker."""
    hist = yf.download(ticker, period="1y", interval="1d", progress=False)
    if hist.empty:
        return {"MA50": None, "MA200": None}
    close = hist["Close"]
    ma50 = close.rolling(window=50).mean().iloc[-1]
    ma200 = close.rolling(window=200).mean().iloc[-1]
    return {"MA50": ma50, "MA200": ma200}


def collect_data() -> pd.DataFrame:
    """Fetch fundamentals and technicals for all tickers."""
    records = []
    for ticker in TICKERS:
        fundamentals = fetch_fundamental_data(ticker)
        technicals = fetch_technical_data(ticker)
        fundamentals.update(technicals)
        records.append(fundamentals)
    return pd.DataFrame(records)


def save_to_csv(df: pd.DataFrame, path: str) -> None:
    """Save the data frame to a CSV file."""
    df.to_csv(path, index=False)


if __name__ == "__main__":
    df = collect_data()
    save_to_csv(df, "data/nifty50_fundamentals.csv")
    print(f"Saved data for {len(df)} tickers.")
