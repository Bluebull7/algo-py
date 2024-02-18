# PORTFOLIO CLASS
import pandas as pd 
import numpy as np 
import datetime as dt
class Portfolio:
    def __init__(self):
        self.positions = {}

    def execute_trades(self.signals, historical_data):

        # <TODO> implement me
        pass
    
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
