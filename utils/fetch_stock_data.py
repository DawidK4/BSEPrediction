import yfinance as yf
import pandas as pd
import pytz

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

def fetch_income_statement(ticker: str, period: str='annual') -> pd.DataFrame:
    """
    Fetch income statement data for a given stock ticker.

    Parameters:
    ticker (str): Stock ticker symbol.
    period (str): 'annual' or 'quarterly'.

    Returns:
    pd.DataFrame: DataFrame containing income statement data.
    """
    stock = yf.Ticker(ticker)
    if period == 'annual':
        return stock.financials
    elif period == 'quarterly':
        return stock.quarterly_financials
    else:
        raise ValueError("Invalid period. Use 'annual' or 'quarterly'.")

def fetch_balance_sheet(ticker: str, period: str='annual') -> pd.DataFrame:
    """
    Fetch balance sheet data for a given stock ticker.

    Parameters:
    ticker (str): Stock ticker symbol.
    period (str): 'annual' or 'quarterly'.

    Returns:
    pd.DataFrame: DataFrame containing balance sheet data.
    """
    stock = yf.Ticker(ticker)
    if period == 'annual':
        return stock.balance_sheet
    elif period == 'quarterly':
        return stock.quarterly_balance_sheet
    else:
        raise ValueError("Invalid period. Use 'annual' or 'quarterly'.")

def fetch_cash_flow(ticker: str, period: str='annual') -> pd.DataFrame:
    """
    Fetch cash flow data for a given stock ticker.

    Parameters:
    ticker (str): Stock ticker symbol.
    period (str): 'annual' or 'quarterly'.

    Returns:
    pd.DataFrame: DataFrame containing cash flow data.
    """
    stock = yf.Ticker(ticker)
    if period == 'annual':
        return stock.cashflow
    elif period == 'quarterly':
        return stock.quarterly_cashflow
    else:
        raise ValueError("Invalid period. Use 'annual' or 'quarterly'.")

def fetch_ttm_cash_flow(ticker: str) ->pd.Series:
    """
    Fetch trailing twelve months (TTM) cash flow data for a given stock ticker.

    Parameters:
    ticker (str): Stock ticker symbol.

    Returns:
    pd.Series: Series containing TTM cash flow data.
    """
    stock = yf.Ticker(ticker)
    cashflow = stock.cashflow
    if cashflow.empty or cashflow.shape[1] < 4:
        raise ValueError("Not enough data to compute TTM cash flow.")
    ttm_cash_flow = cashflow.iloc[:, :4].sum(axis=1)
    return ttm_cash_flow

def fetch_earnings(ticker: str) -> pd.DataFrame:
    """
    Fetch earnings data for a given stock ticker.

    Parameters:
    ticker (str): Stock ticker symbol.

    Returns:
    pd.DataFrame: DataFrame containing earnings data.
    """
    stock = yf.Ticker(ticker)
    return stock.earnings

if __name__ == "__main__":
    # Example usage
    ticker = "AAPL"
    ohlc_data = fetch_ohlc(ticker, period='1y', interval='1d')
    volume_data = fetch_volume(ticker, period='1y', interval='1d')
    dividend_data = fetch_dividends(ticker, period='1y')
    split_data = fetch_splits(ticker, period='1y')
    capital_gains_data = fetch_capital_gains(ticker, period='1y')
    income_statement = fetch_income_statement(ticker, period='annual')
    balance_sheet = fetch_balance_sheet(ticker, period='annual')
    cash_flow = fetch_cash_flow(ticker, period='annual')
    ttm_cash_flow = fetch_ttm_cash_flow(ticker)
    earnings = fetch_earnings(ticker)

    # print("OHLC Data:")
    # print(ohlc_data.head())
    # print("\nVolume Data:")
    # print(volume_data.head())
    # print("\nDividend Data:")
    # print(dividend_data.head())
    # print("\nSplit Data:")
    # print(split_data.head())
    # print("\nCapital Gains Data:")
    # print(capital_gains_data.head())
    print("\nIncome Statement:")
    print(income_statement.head())
    print("\nBalance Sheet:")
    print(balance_sheet.head())
    print("\nCash Flow:")
    print(cash_flow.head())
    print("\nTTM Cash Flow:")
    print(ttm_cash_flow.head())
    print("\nEarnings:")
    print(type(earnings))
    print(earnings)