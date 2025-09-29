from utils import save_data

def main():
    path = '/home/dawid/projects/BSEPrediction/AAPL/data'

    utils.save_data.save_financial_info('AAPL', path)
    utils.save_data.save_price_and_volume('AAPL', path)
    utils.save_data.save_financials('AAPL', path)
    utils.save_data.save_analyst_info('AAPL', path)
    utils.save_data.save_holders_info('AAPL', path)
    utils.save_data.save_calendar_info('AAPL', path)

if __name__ == "__main__":
    main()