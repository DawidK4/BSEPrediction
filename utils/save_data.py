from utils.fetch_stock_data import *
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
    if ohlc_data.empty is not None:
        ohlc_data.to_csv(ohlc_file)

    volume_data = fetch_volume(ticker)
    volume_file = os.path.join(filepath, f'{ticker}_volume.csv')
    if volume_data.empty is not None:
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
    if dividends_data.empty is not None:
        dividends_data.to_csv(os.path.join(filepath, f'{ticker}_dividends.csv'), header=['Dividends'])

    splits_data = fetch_splits(ticker)
    if splits_data.empty is not None:
        splits_data.to_csv(os.path.join(filepath, f'{ticker}_splits.csv'), header=['Splits'])

    capital_gains_data = fetch_capital_gains(ticker)
    if capital_gains_data.empty is not None:
        capital_gains_data.to_csv(os.path.join(filepath, f'{ticker}_capital_gains.csv'), header=['Capital Gains'])

    actions = data.actions
    if actions.empty is not None:
        actions.to_csv(os.path.join(filepath, f'{ticker}_actions.csv'))

    income_stmt = data.income_stmt
    if income_stmt.empty is not None:
        income_stmt.to_csv(os.path.join(filepath, f'{ticker}_income_statement.csv'))

    balance_sheet = data.balance_sheet
    if balance_sheet.empty is not None:
        balance_sheet.to_csv(os.path.join(filepath, f'{ticker}_balance_sheet.csv'))

    cash_flow = data.cash_flow
    if cash_flow.empty is not None:
        cash_flow.to_csv(os.path.join(filepath, f'{ticker}_cash_flow.csv'))

    ttm_cash_flow = data.ttm_cash_flow
    if ttm_cash_flow.empty is not None:
        ttm_cash_flow.to_csv(os.path.join(filepath, f'{ticker}_ttm_cash_flow.csv'))

    earnings = data.earnings
    if earnings.empty is not None:
        earnings.to_csv(os.path.join(filepath, f'{ticker}_earnings.csv'))

    info = pd.Series(data.info)
    if info.empty is not None:
        info.to_csv(os.path.join(filepath, f'{ticker}_info.csv'), header=['Info'])

    calendar = pd.Series(data.calendar)
    if calendar.empty is not None:
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
    if sustainability.empty is not None:
        sustainability.to_csv(os.path.join(filepath, f'{ticker}_sustainability.csv'))

    recommendations = data.recommendations
    if recommendations.empty is not None:
        recommendations.to_csv(os.path.join(filepath, f'{ticker}_recommendations.csv'))

    institutional_holders = data.institutional_holders
    if institutional_holders.empty is not None:
        institutional_holders.to_csv(os.path.join(filepath, f'{ticker}_institutional_holders.csv'))

    mutualfund_holders = data.mutualfund_holders
    if mutualfund_holders.empty is not None:
        mutualfund_holders.to_csv(os.path.join(filepath, f'{ticker}_mutualfund_holders.csv'))

    options = pd.DataFrame(data.options, columns=['Options'])
    if options.empty is not None:
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
    if analysis.empty is not None:
        analysis.to_csv(os.path.join(filepath, f'{ticker}_analysis.csv'))

    earnings_history = pd.DataFrame(data.earnings_history)
    if earnings_history.empty is not None:
        earnings_history.to_csv(os.path.join(filepath, f'{ticker}_earnings_history.csv'), index=False)

    earnings_trend = pd.DataFrame(data.earnings_trend)
    if earnings_trend.empty is not None:
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
    if funds_data.empty is not None:
        funds_data.to_csv(os.path.join(filepath, f'{ticker}_funds_data.csv'))

    insider_purchases = data.insider_purchases
    if insider_purchases.empty is not None:
        insider_purchases.to_csv(os.path.join(filepath, f'{ticker}_insider_purchases.csv'))

    insider_transactions = data.insider_transactions
    if insider_transactions.empty is not None:
        insider_transactions.to_csv(os.path.join(filepath, f'{ticker}_insider_transactions.csv'))

    insider_roster_holders = data.insider_roster_holders
    if insider_roster_holders.empty is not None:
        insider_roster_holders.to_csv(os.path.join(filepath, f'{ticker}_insider_roster_holders.csv'))

    major_holders = data.major_holders
    if major_holders.empty is not None:
        major_holders.to_csv(os.path.join(filepath, f'{ticker}_major_holders.csv'))

    institutional_holder = data.institutional_holder
    if institutional_holder.empty is not None:
        institutional_holder.to_csv(os.path.join(filepath, f'{ticker}_institutional_holder.csv'))

    mutualfund_holders = data.mutualfund_holders
    if mutualfund_holders.empty is not None:
        mutualfund_holders.to_csv(os.path.join(filepath, f'{ticker}_mutualfund_holders.csv'))

    print(f"Holdings info for {ticker} saved to CSV files in {filepath}.")
