from portfolio import portfolio
from strategy import strategy
from data_source import data_source

class TradingAlgorithm:
    
    def __init__(self,data_source):
        self.data_source = data_source
        self.portfolio = Portfolio()
        self.strategy = Strategy()


    def run_backtest(self):
        historical_data = self.data_source.fetch_data()
        # signals
        # execute
        # calculate performance
