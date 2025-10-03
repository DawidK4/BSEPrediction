import yfinance as yf
import pandas as pd

def fetch_ohlc_and_volume(ticker: str, period: str='max', interval: str='1d') -> pd.DataFrame:
    """
    Fetch OHLC data for a given stock ticker.

    Parameters:
    ticker (str): Stock ticker symbol.
    period (str): Data period to download (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').
    interval (str): Data interval (e.g., '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo').

    Returns:
    pd.DataFrame: DataFrame containing OHLC data.
    """
    data = yf.download(ticker, period=period, interval=interval)

    return data

def fetch_dividends(ticker: str, period: str='max') -> pd.Series:
    """
    Fetch dividend data for a given stock ticker.

    Parameters:
    ticker (str): Stock ticker symbol.
    period (str): Data period to download (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').

    Returns:
    pd.Series: Series containing dividend data.
    """
    stock = yf.Ticker(ticker)
    dividends = stock.dividends
    if period != 'max':
        end_date = pd.Timestamp.today()
        if dividends.index.tz is not None:
            tz = dividends.index.tz
            end_date = end_date.tz_localize(tz)
        if period.endswith('d'):
            start_date = end_date - pd.Timedelta(days=int(period[:-1]))
        elif period.endswith('mo'):
            start_date = end_date - pd.DateOffset(months=int(period[:-2]))
        elif period.endswith('y'):
            start_date = end_date - pd.DateOffset(years=int(period[:-1]))
        else:
            raise ValueError("Invalid period format. Use 'd' for days, 'mo' for months, or 'y' for years.")
        dividends = dividends[(dividends.index >= start_date) & (dividends.index <= end_date)]
    return dividends

def fetch_splits(ticker: str, period: str='max') -> pd.Series:
    """
    Fetch stock split data for a given stock ticker.

    Parameters:
    ticker (str): Stock ticker symbol.
    period (str): Data period to download (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').

    Returns:
    pd.Series: Series containing stock split data.
    """
    stock = yf.Ticker(ticker)
    splits = stock.splits
    if period != 'max':
        end_date = pd.Timestamp.today()
        if splits.index.tz is not None:
            tz = splits.index.tz
            end_date = end_date.tz_localize(tz)
        if period.endswith('d'):
            start_date = end_date - pd.Timedelta(days=int(period[:-1]))
        elif period.endswith('mo'):
            start_date = end_date - pd.DateOffset(months=int(period[:-2]))
        elif period.endswith('y'):
            start_date = end_date - pd.DateOffset(years=int(period[:-1]))
        else:
            raise ValueError("Invalid period format. Use 'd' for days, 'mo' for months, or 'y' for years.")
        splits = splits[(splits.index >= start_date) & (splits.index <= end_date)]
    return splits

def fetch_capital_gains(ticker: str, period: str='max') -> pd.Series:
    """
    Fetch capital gains data for a given stock ticker.

    Parameters:
    ticker (str): Stock ticker symbol.
    period (str): Data period to download (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').

    Returns:
    pd.Series: Series containing capital gains data.
    """
    stock = yf.Ticker(ticker)
    # Note: yfinance does not provide a direct method to fetch capital gains.
    # This is a placeholder implementation and may need to be adjusted based on actual data availability.
    capital_gains = stock.actions.get('Capital Gains', pd.Series(dtype=float))
    if period != 'max' and not capital_gains.empty:
        end_date = pd.Timestamp.today()
        if capital_gains.index.tz is not None:
            tz = capital_gains.index.tz
            end_date = end_date.tz_localize(tz)
        if period.endswith('d'):
            start_date = end_date - pd.Timedelta(days=int(period[:-1]))
        elif period.endswith('mo'):
            start_date = end_date - pd.DateOffset(months=int(period[:-2]))
        elif period.endswith('y'):
            start_date = end_date - pd.DateOffset(years=int(period[:-1]))
        else:
            raise ValueError("Invalid period format. Use 'd' for days, 'mo' for months, or 'y' for years.")
        capital_gains = capital_gains[(capital_gains.index >= start_date) & (capital_gains.index <= end_date)]
    return capital_gains
