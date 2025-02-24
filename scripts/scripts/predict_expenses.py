import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

def predict_expenses(df):
    """Predicts future expenses using ARIMA model."""
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)

    model = ARIMA(df["Amount"], order=(1, 1, 1))
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=1)

    return forecast

if __name__ == "__main__":
    df = pd.read_csv("data/transactions.csv")
    prediction = predict_expenses(df)
    print(f"Next month's predicted expense: ${prediction[0]:.2f}")
