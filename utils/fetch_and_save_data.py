import pandas as pd
import yfinance as yf
import os

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

def get_financials(ticker: str) -> list[pd.DataFrame]:
    """
    Fetch financial statements for a given stock ticker.

    Parameters:
    ticker (str): Stock ticker symbol.

    Returns:
    list[pd.DataFrame]: List containing DataFrames of balance sheet, cash flow, and earnings.
    """
    stock = yf.Ticker(ticker)

    income_statement = stock.income_stmt
    # ttm_income_statement = stock.income_stmt_ttm
    balance_sheet = stock.balance_sheet
    cashflow = stock.cashflow
    # ttm_cash_flow = stock.cashflow_ttm
    # earnings = stock.earnings
    calendar = stock.calendar
    # earnings_dates = stock.earnings_dates
    sec_filings = stock.sec_filings

    return [income_statement, balance_sheet,
            cashflow, calendar, sec_filings]


def get_analysis_and_holdings(ticker: str) -> list[pd.DataFrame]:
    """
    Fetch analysis and holdings data for a given stock ticker.

    Parameters:
    ticker (str): Stock ticker symbol.

    Returns:
    list[pd.DataFrame]: List containing DataFrames of analysis and holdings.
    """
    stock = yf.Ticker(ticker)

    recommendations = stock.recommendations
    upgrades_downgrades = stock.upgrades_downgrades
    sustainability = stock.sustainability
    analyst_price_targets = stock.analyst_price_targets
    earnings_estimate = stock.earnings_estimate
    revenue_estimate = stock.revenue_estimate
    earnings_history = stock.earnings_history
    eps_trend = stock.eps_trend
    eps_revisions = stock.eps_revisions
    growth_estimates = stock.growth_estimates
    funds_data = stock.funds_data
    insider_purchases = stock.insider_purchases
    insider_roster_holders = stock.insider_roster_holders
    major_holders = stock.major_holders
    institutional_holders = stock.institutional_holders
    mutualfund_holders  = stock.mutualfund_holders

    return  [recommendations, upgrades_downgrades, sustainability,
            analyst_price_targets, earnings_estimate, revenue_estimate,
            earnings_history, eps_trend, eps_revisions, growth_estimates,
            funds_data, insider_purchases, insider_roster_holders, major_holders,
            institutional_holders, mutualfund_holders]

def download_and_save_VIX(period: str='max', interval: str='1d') -> None:
    """
    Fetch VIX index data.

    Parameters:
    period (str): Data period to download (e.g., '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max').
    interval (str): Data interval (e.g., '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo').

    """
    vix_data = yf.download('^VIX', period=period, interval=interval)

    os.makedirs('VIX/data/price', exist_ok=True)
    vix_data.to_csv('VIX/data/price/VIX_price_volume.csv')

def download_and_save_data(ticker: str) -> None:
    """
    Download and save various stock data to CSV files.

    Parameters:
    ticker (str): Stock ticker symbol.
    """
    base_path = f"{ticker}/data/"
    subfolders = ['price', 'info', 'financials', 'analysis_and_holdings']

    # Create all necessary directories
    for folder in subfolders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    # Fetch and save price and volume data
    price_volume_data = get_price_and_volume(ticker)
    price_volume_data.to_csv(os.path.join(base_path, 'price', f"{ticker}_price_volume.csv"))

    # Fetch and save stock data
    stock_data = get_stock_data(ticker)
    stock_data_names = ['isin', 'history', 'dividends', 'splits', 'actions',
                        'capital_gains', 'info', 'fast_info', 'news']
    for data, name in zip(stock_data, stock_data_names):
        if isinstance(data, (pd.DataFrame, pd.Series)):
            data.to_csv(os.path.join(base_path, 'info', f"{ticker}_{name}.csv"))

    # Fetch and save financial statements
    financials = get_financials(ticker)
    financials_names = ['income_statement', 'balance_sheet',
                        'cashflow', 'calendar', 'sec_filings']
    for data, name in zip(financials, financials_names):
        if isinstance(data, (pd.DataFrame, pd.Series)):
            data.to_csv(os.path.join(base_path, 'financials', f"{ticker}_{name}.csv"))

    # Fetch and save analysis and holdings data
    analysis_holdings = get_analysis_and_holdings(ticker)
    analysis_holdings_names = ['recommendations', 'upgrades_downgrades', 'sustainability',
                               'analyst_price_targets', 'earnings_estimate', 'revenue_estimate',
                               'earnings_history', 'eps_trend', 'eps_revisions', 'growth_estimates',
                               'funds_data', 'insider_purchases', 'insider_roster_holders', 'major_holders',
                               'institutional_holders', 'mutualfund_holders']
    for data, name in zip(analysis_holdings, analysis_holdings_names):
        if isinstance(data, (pd.DataFrame, pd.Series)):
            data.to_csv(os.path.join(base_path, 'analysis_and_holdings', f"{ticker}_{name}.csv"))


