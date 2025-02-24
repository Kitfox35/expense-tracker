import pandas as pd

CATEGORY_MAP = {
    "Walmart": "Groceries",
    "Uber": "Transport",
    "Amazon": "Shopping",
    "Coffee Bean": "Food & Drinks"
}

def categorize_transactions(df):
    """Assign categories based on transaction descriptions."""
    df["Category"] = df["Description"].apply(lambda x: CATEGORY_MAP.get(x, "Other"))
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/transactions.csv")
    df = categorize_transactions(df)
    print(df.head())
