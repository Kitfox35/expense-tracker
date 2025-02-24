# add transaction fetch script
import pandas as pd

def fetch_transactions(file_path="data/transactions.csv"):
    """Loads transaction data from a CSV file."""
    df = pd.read_csv(file_path)
    return df

if __name__ == "__main__":
    df = fetch_transactions()
    print(df.head())
