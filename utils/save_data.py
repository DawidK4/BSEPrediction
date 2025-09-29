from fetch_stock_data import *
import os

def save_price_and_volume(ticker: str, filepath: str) -> None:
    """
    Fetch and save stock OHLCV for a given ticker to CSV files.

    Parameters:
    ticker (str): Stock ticker symbol.
    filepath (str): Directory path to save CSV files.
    """
    ohlc_data = fetch_ohlc(ticker)
    ohlc_file = os.path.join(filepath, f'{ticker}_ohlc.csv')
    ohlc_data.to_csv(ohlc_file)

    volume_data = fetch_volume(ticker)
    volume_file = os.path.join(filepath, f'{ticker}_volume.csv')
    volume_data.to_csv(volume_file, header=['Volume'])

    print(f"OHLCV for {ticker} saved to CSV files in {filepath}.")


def save_financials(ticker: str, filepath: str) -> None:
    """
    Fetch and save various financial data for a given ticker to CSV files.

    Parameters:
    ticker (str): Stock ticker symbol.
    filepath (str): Directory path to save CSV files.
    """
    data = yf.Ticker(ticker)

    dividends_data = fetch_dividends(ticker)
    dividends_data.to_csv(os.path.join(filepath, f'{ticker}_dividends.csv'), header=['Dividends'])

    splits_data = fetch_splits(ticker)
    splits_data.to_csv(os.path.join(filepath, f'{ticker}_splits.csv'), header=['Splits'])

    capital_gains_data = fetch_capital_gains(ticker)
    capital_gains_data.to_csv(os.path.join(filepath, f'{ticker}_capital_gains.csv'), header=['Capital Gains'])

    actions = data.actions
    actions.to_csv(os.path.join(filepath, f'{ticker}_actions.csv'))

    income_stmt = data.income_stmt
    income_stmt.to_csv(os.path.join(filepath, f'{ticker}_income_statement.csv'))

    balance_sheet = data.balance_sheet
    balance_sheet.to_csv(os.path.join(filepath, f'{ticker}_balance_sheet.csv'))

    cash_flow = data.cash_flow
    cash_flow.to_csv(os.path.join(filepath, f'{ticker}_cash_flow.csv'))

    ttm_cash_flow = data.ttm_cash_flow
    ttm_cash_flow.to_csv(os.path.join(filepath, f'{ticker}_ttm_cash_flow.csv'))

    earnings = data.earnings
    earnings.to_csv(os.path.join(filepath, f'{ticker}_earnings.csv'))

    info = pd.Series(data.info)
    info.to_csv(os.path.join(filepath, f'{ticker}_info.csv'), header=['Info'])

    calendar = pd.Series(data.calendar)
    calendar.to_csv(os.path.join(filepath, f'{ticker}_calendar.csv'), header=['Calendar'])

    print(f"Financial info for {ticker} saved to CSV files in {filepath}.")

def save_additional_info(ticker: str, filepath: str) -> None:
    """
    Fetch and save additional stock data for a given ticker to CSV files.

    Parameters:
    ticker (str): Stock ticker symbol.
    filepath (str): Directory path to save CSV files.
    """
    data = yf.Ticker(ticker)

    sustainability = pd.DataFrame(data.sustainability)
    sustainability.to_csv(os.path.join(filepath, f'{ticker}_sustainability.csv'))

    recommendations = data.recommendations
    recommendations.to_csv(os.path.join(filepath, f'{ticker}_recommendations.csv'))

    institutional_holders = data.institutional_holders
    institutional_holders.to_csv(os.path.join(filepath, f'{ticker}_institutional_holders.csv'))

    mutualfund_holders = data.mutualfund_holders
    mutualfund_holders.to_csv(os.path.join(filepath, f'{ticker}_mutualfund_holders.csv'))

    options = pd.DataFrame(data.options, columns=['Options'])
    options.to_csv(os.path.join(filepath, f'{ticker}_options.csv'), index=False)

    print(f"Additional info for {ticker} saved to CSV files in {filepath}.")

def save_analysis(ticker: str, filepath: str) -> None:
    """
    Fetch and save stock analysis data for a given ticker to CSV files.

    Parameters:
    ticker (str): Stock ticker symbol.
    filepath (str): Directory path to save CSV files.
    """
    data = yf.Ticker(ticker)

    analysis = data.analysis
    analysis.to_csv(os.path.join(filepath, f'{ticker}_analysis.csv'))

    earnings_history = pd.DataFrame(data.earnings_history)
    earnings_history.to_csv(os.path.join(filepath, f'{ticker}_earnings_history.csv'), index=False)

    earnings_trend = pd.DataFrame(data.earnings_trend)
    earnings_trend.to_csv(os.path.join(filepath, f'{ticker}_earnings_trend.csv'), index=False)

    print(f"Analysis info for {ticker} saved to CSV files in {filepath}.")

def save_holdings(ticker: str, filepath: str) -> None:
    """
    Fetch and save stock holdings data for a given ticker to CSV files.

    Parameters:
    ticker (str): Stock ticker symbol.
    filepath (str): Directory path to save CSV files.
    """
    data = yf.Ticker(ticker)

    funds_data = data.funds_data
    funds_data.to_csv(os.path.join(filepath, f'{ticker}_funds_data.csv'))

    insider_purchases = data.insider_purchases
    insider_purchases.to_csv(os.path.join(filepath, f'{ticker}_insider_purchases.csv'))

    insider_transactions = data.insider_transactions
    insider_transactions.to_csv(os.path.join(filepath, f'{ticker}_insider_transactions.csv'))

    insider_roster_holders = data.insider_roster_holders
    insider_roster_holders.to_csv(os.path.join(filepath, f'{ticker}_insider_roster_holders.csv'))

    major_holders = data.major_holders
    major_holders.to_csv(os.path.join(filepath, f'{ticker}_major_holders.csv'))

    institutional_holder = data.institutional_holder
    institutional_holder.to_csv(os.path.join(filepath, f'{ticker}_institutional_holder.csv'))

    mutualfund_holders = data.mutualfund_holders
    mutualfund_holders.to_csv(os.path.join(filepath, f'{ticker}_mutualfund_holders.csv'))

    print(f"Holdings info for {ticker} saved to CSV files in {filepath}.")
