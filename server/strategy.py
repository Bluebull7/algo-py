# Strategy Class

import numpy as numpy

class Strategy:
    @staticmethod
    def generate_ema_signals(close_prices, window):
    ema = close_prices.ewm(span=window, adjust = False).mean()
    signal = np.where(close_prices > ema, 1, 0,) # 1 for Buy, 0 for Hold
    signals = np.where(close_prices < ema, -1, signals) # -1 for Sell
    return signals



