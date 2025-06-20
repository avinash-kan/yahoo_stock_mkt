from src.etl import collect_data, save_to_csv


def main():
    df = collect_data()
    save_to_csv(df, "data/nifty50_fundamentals.csv")
    print(f"Saved data for {len(df)} tickers.")


if __name__ == "__main__":
    main()
