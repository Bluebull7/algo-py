from portfolio import portfolio
from strategy import strategy
from data_source import data_source
from portfolio import create_portfolio

class TradingAlgorithm:
    
    def __init__(self,data_source):
        self.data_source = data_source
        self.portfolio = Portfolio()
        self.strategy = Strategy()


    def run_backtest(self):
        historical_data = self.data_source.fetch_data()
        portfolio = create_portfolio(portfolio)

        # Loop through the data
        for date, row in historical_data.iterrows():
            # get the close price
            close_price = row["Close"]
            # get the signal
            signal = self.strategy.generate_ema_signal(close_price, window=20)
            # execute the trade
            self.portfolio.execute_trade(date, close_price, signal)
        # calculate performance
