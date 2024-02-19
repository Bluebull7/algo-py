# PORTFOLIO CLASS
import numpy as np
from typing import List
from strategy import Strategy


class Portfolio:
    def __init__(self, initial_balance=100000.00):
        self.positions = {}
        self.cash_balance = initial_balance
        self.transaction_history = []
        self.strategy = Strategy()

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

            self.transaction_history.append(
                {
                    "Date": date,
                    "Action": "Sell",
                    "Price": price,
                    "Shares": shares_to_sell,
                }
            )

    def calculate_performance(self, final_date, initial_balance):
        
        self.initial_balance = initial_balance
        # Calculate portfolio performance metrics
        
        if not self.transaction_history:
            print("No transaction executed. Performance cannot be calculated")
            return
        else:
        # sort the transaction history by date
            sorted_transactions = sorted(self.transaction_history, key=lambda x: x['Date'])
        # calculate cumulative returns
            cumulative_returns = 0.0
            portfolio_value_over_time = []

            for transaction in sorted_transactions:
                if transaction['Action'] == 'Buy':
                    cumulative_returns -= transaction['Shares'] * transaction['Price']
                elif transaction['Action'] == 'Sell':
                    cumulative_returns += transaction['Shares'] * transaction['Price']
            portfolio_value = self.cash_balance + cumulative_returns
            portfolio_value_over_time.append((transaction['Date'], portfolio_value))

        # calculate total returns
            total_returns = (portfolio_value_over_time[-1][1] - initial_balance) / initial_balance * 1000.00

        #print/return performance metrics
            print(f"Total Returns: {total_returns:.2f}%")
            print(f"Final Portfolio Value on {final_date}: {portfolio_value_over_time[-1][1]:.2f}")

