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
    if not ohlc_data.empty:
        ohlc_data.to_csv(ohlc_file)

    volume_data = fetch_volume(ticker)
    volume_file = os.path.join(filepath, f'{ticker}_volume.csv')
    if not volume_data.empty:
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
    if not dividends_data.empty:
        dividends_data.to_csv(os.path.join(filepath, f'{ticker}_dividends.csv'), header=['Dividends'])

    splits_data = fetch_splits(ticker)
    if not splits_data.empty:
        splits_data.to_csv(os.path.join(filepath, f'{ticker}_splits.csv'), header=['Splits'])

    capital_gains_data = fetch_capital_gains(ticker)
    if not capital_gains_data.empty:
        capital_gains_data.to_csv(os.path.join(filepath, f'{ticker}_capital_gains.csv'), header=['Capital Gains'])

    actions = data.actions
    if not actions.empty:
        actions.to_csv(os.path.join(filepath, f'{ticker}_actions.csv'))

    income_stmt = data.income_stmt
    if not income_stmt.empty:
        income_stmt.to_csv(os.path.join(filepath, f'{ticker}_income_statement.csv'))

    balance_sheet = data.balance_sheet
    if not balance_sheet.empty:
        balance_sheet.to_csv(os.path.join(filepath, f'{ticker}_balance_sheet.csv'))

    cash_flow = data.cash_flow
    if not cash_flow.empty:
        cash_flow.to_csv(os.path.join(filepath, f'{ticker}_cash_flow.csv'))

    ttm_cash_flow = data.ttm_cash_flow
    if not ttm_cash_flow.empty:
        ttm_cash_flow.to_csv(os.path.join(filepath, f'{ticker}_ttm_cash_flow.csv'))

    earnings = data.earnings
    if not earnings.empty:
        earnings.to_csv(os.path.join(filepath, f'{ticker}_earnings.csv'))

    info = pd.Series(data.info)
    if not info.empty:
        info.to_csv(os.path.join(filepath, f'{ticker}_info.csv'), header=['Info'])

    calendar = pd.Series(data.calendar)
    if not calendar.empty:
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
    if not sustainability.empty:
        sustainability.to_csv(os.path.join(filepath, f'{ticker}_sustainability.csv'))

    recommendations = data.recommendations
    if not recommendations.empty:
        recommendations.to_csv(os.path.join(filepath, f'{ticker}_recommendations.csv'))

    institutional_holders = data.institutional_holders
    if not institutional_holders.empty:
        institutional_holders.to_csv(os.path.join(filepath, f'{ticker}_institutional_holders.csv'))

    mutualfund_holders = data.mutualfund_holders
    if not mutualfund_holders.empty:
        mutualfund_holders.to_csv(os.path.join(filepath, f'{ticker}_mutualfund_holders.csv'))

    options = pd.DataFrame(data.options, columns=['Options'])
    if not options.empty:
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
    if not analysis.empty:
        analysis.to_csv(os.path.join(filepath, f'{ticker}_analysis.csv'))

    earnings_history = pd.DataFrame(data.earnings_history)
    if not earnings_history.empty:
        earnings_history.to_csv(os.path.join(filepath, f'{ticker}_earnings_history.csv'), index=False)

    earnings_trend = pd.DataFrame(data.earnings_trend)
    if not earnings_trend.empty:
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
    if not funds_data.empty:
        funds_data.to_csv(os.path.join(filepath, f'{ticker}_funds_data.csv'))

    insider_purchases = data.insider_purchases
    if not insider_purchases.empty:
        insider_purchases.to_csv(os.path.join(filepath, f'{ticker}_insider_purchases.csv'))

    insider_transactions = data.insider_transactions
    if not insider_transactions.empty:
        insider_transactions.to_csv(os.path.join(filepath, f'{ticker}_insider_transactions.csv'))

    insider_roster_holders = data.insider_roster_holders
    if not insider_roster_holders.empty:
        insider_roster_holders.to_csv(os.path.join(filepath, f'{ticker}_insider_roster_holders.csv'))

    major_holders = data.major_holders
    if not major_holders.empty:
        major_holders.to_csv(os.path.join(filepath, f'{ticker}_major_holders.csv'))

    institutional_holder = data.institutional_holder
    if not institutional_holder.empty:
        institutional_holder.to_csv(os.path.join(filepath, f'{ticker}_institutional_holder.csv'))

    mutualfund_holders = data.mutualfund_holders
    if not mutualfund_holders.empty:
        mutualfund_holders.to_csv(os.path.join(filepath, f'{ticker}_mutualfund_holders.csv'))

    print(f"Holdings info for {ticker} saved to CSV files in {filepath}.")
