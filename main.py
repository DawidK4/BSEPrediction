import utils

def save_aapl():
    path = '/home/dawid/projects/BSEPrediction/AAPL/data'
    ticker = 'AAPL'

    # utils.save_price_and_volume(ticker, path)
    # utils.save_financials(ticker, path)
    # utils.save_additional_info(ticker, path)
    # utils.save_analysis(ticker, path)
    # utils.save_holdings(ticker, path)
    utils.save_splits(ticker, path)

if __name__ == "__main__":
    save_aapl()