import utils

if __name__ == "__main__":
    l = utils.get_price_and_volume("AAPL")
    l1 = utils.get_stock_data("AAPL")
    l2 = utils.get_financials("AAPL")
    l3 = utils.get_analysis_and_holdings("AAPL")
    print(l3)