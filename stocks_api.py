import yfinance as yf


def get_stock_price_by_symbol(symbol):
    history = yf.Ticker(symbol).history(period='min')
    return history.iloc[0, 3]


def get_last_month_by_symbol(symbol):
    last_month = yf.Ticker(symbol).history(period="1mo")
    print("generate_chart")

