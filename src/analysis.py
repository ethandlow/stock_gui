import ta

def simple_moving_average(data):
    sma_20 = ta.trend.sma_indicator(data['Close'], window=20)
    return sma_20