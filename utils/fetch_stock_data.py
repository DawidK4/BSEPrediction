import yfinance as yf
import pandas as pd

def fetch_ohlc(ticker: str, period: str='max', interval: str='1d') -> pd.DataFrame:
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
    data = data.drop('Volume', axis=1)

    return data

def fetch_volume(ticker: str, period: str='max', interval: str='1d') -> pd.Series:
    """
    Fetch volume data for a given stock ticker.

    Parameters:
    ticker (str): Stock ticker symbol.
    period (str): Data period to download (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').
    interval (str): Data interval (e.g., '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo').

    Returns:
    pd.Series: Series containing volume data.
    """
    data = yf.download(ticker, period=period, interval=interval)
    return data['Volume']

if __name__ == "__main__":
    # Example usage
    ticker = "AAPL"
    ohlc_data = fetch_ohlc(ticker, period='1y', interval='1d')
    print(ohlc_data.head())

    volume_data = fetch_volume(ticker, period='1y', interval='1d')
    print(volume_data.head())