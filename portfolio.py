#PORTFOLIO CLASS
from typing import List
import pandas as pd 
import numpy as np 
import datetime as dt
from strategy import Strategy

class Portfolio:
    def __init__(self, initial_balance=100000.00):
        self.positions = {}
        self.cash_balance = initial_balance
        self.transaction_history = []
    def execute_trades(self, close_prices):

        # <TODO> implement me
        signals = Strategy.generate_ema_signals(close_prices, window=50)

        for i in range(1, len(signals)):
            if signals[i] == 1 and signals[i - 1] == 0:
                #buy signals
                self.buy(historical_data.index[i], historical_data['Close'][i])
            elif signals[i] == -1 and signals[i-1] ==0:
                # sell signal
                self.sell(historical_data.index[i], historical_data['Close'][i])
        
    
    def generate_ema_signal(self, close_price, window):
        ema = close_price.ewm(span=window, adjust=False).mean()
        # 1 -> buy, 0 -> hold
        signals = np.where(close_price > ema, 1, 0)
        # -1 -> sell
        signals = np.where(close_price < ema, -1, signals)
        
        return signals


    def buy(self, date, price):
        pass

    def sell(self, date, price):
        pass
    
    def calculate_performance(self):

        # <TODO> implement me

        # Calculate portfolio performance metrics
        # print/return perf results

        pass
