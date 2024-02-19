# PORTFOLIO CLASS
from typing import List
import pandas as pd
import numpy as np
import datetime as dt

from pandas.core.indexes.datetimes import DatetimeTimedeltaMixin
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
                # buy signals
                self.buy(historical_data.index[i], historical_data["Close"][i])
            elif signals[i] == -1 and signals[i - 1] == 0:
                # sell signal
                self.sell(historical_data.index[i], historical_data["Close"][i])

    def generate_ema_signal(self, close_price, window):
        ema = close_price.ewm(span=window, adjust=False).mean()
        # 1 -> buy, 0 -> hold
        signals = np.where(close_price > ema, 1, 0)
        # -1 -> sell
        signals = np.where(close_price < ema, -1, signals)

        return signals

    def buy(self, date, price):
        # Assume fixed investment amount for each trade
        investment_amount = 1000.00

        # calculate shares
        shares_to_buy = investment_amount / price

        # check if there is enough cash to execute trade
        if shares_to_buy * price > self.cash_balance:
            print(f"Not enough cash to buy on {date}...")
            return

        # update the position and the cash cash_balance
        elif date not in self.positions:
            self.positions[date] = 100000.00

            self.positions += shares_to_buy
            self.cash_balance -= shares_to_buy * price

            # Record the transaction in transaction_history
            self.transaction_history.append(
                {"Date": date, "Action": "Buy", "Price": price, "Shares": shares_to_buy}
            )

    def sell(self, date, price):
    # check if there is any shares to self
        if date not in self.positions or self.positions[date] == 0:
            print(f"No shares to sell on {date}")
            return

        else:
            shares_to_sell = self.positions[date]

            # update the positions and cash cash_balance
            self.positions[date] = 0 
            self.cash_balance += shares_to_sell * price

            # record the transaction in transaction_history

            self.transaction_history.append({
                'Date': date,
                'Action': 'Sell',
                'Price': price,
                'Shares': shares_to_sell
            })
    

    def calculate_performance(self):

        # <TODO> implement me

        # Calculate portfolio performance metrics
        # print/return perf results

        pass
