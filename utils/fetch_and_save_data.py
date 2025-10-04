import pandas as pd
import yfinance as yf

def get_price_and_volume(ticker: str, period: str='max', interval: str='1d') -> pd.DataFrame:
    """
    Fetch OHLC and volume data for a given stock ticker.

    Parameters:
    ticker (str): Stock ticker symbol.
    period (str): Data period to download (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').
    interval (str): Data interval (e.g., '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo').

    Returns:
    pd.DataFrame: DataFrame containing OHLC and volume data.
    """
    data = yf.download(ticker, period=period, interval=interval)

    return data

def get_stock_data(ticker: str) -> list[pd.DataFrame]:
    """
    Fetch various stock data for a given ticker.

    Parameters:
    ticker (str): Stock ticker symbol.

    Returns:
    list[pd.DataFrame]: List containing DataFrames of dividends, splits, and capital gains.
    """
    stock = yf.Ticker(ticker)

    isin = stock.isin
    history = stock.history(period='max')
    dividends = stock.dividends
    splits = stock.splits
    actions = stock.actions
    capital_gains = stock.capital_gains
    info = pd.Series(stock.info)
    fast_info = pd.Series(stock.fast_info)
    news = stock.news

    return [isin, history, dividends, splits, actions, capital_gains, info, fast_info, news]