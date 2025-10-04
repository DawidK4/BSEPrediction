import pandas as pd
import yfinance as yf

def fetch_price(ticker: str, period: str='max', interval: str='1d') -> list[pd.DataFrame]:
    """
    Fetch various stock data for a given ticker.
    Parameters:
    ticker (str): Stock ticker symbol.
    period (str): Data period to download (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').
    interval (str): Data interval (e.g., '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo').
    Returns:
    list[pd.DataFrame]: List containing DataFrames of OHLCV, dividends, splits, options, and actions.
    """
    result = []

    ohlcv = yf.download(ticker, period=period, interval=interval)
    result.append(ohlcv)

    stock = yf.Ticker(ticker)

    dividends = stock.dividends
    result.append(dividends)

    splits = stock.splits
    result.append(splits)

    options = stock.options
    result.append(options)

    actions = stock.actions
    result.append(actions)

    return result

