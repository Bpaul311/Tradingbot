# import yfinance as yf
# import matplotlib.pyplot as plt

# ticker_symbol = '^IXIC'

# historical_data = yf.download(ticker_symbol, start='2024-01-01', end='2024-05-24')

# closing_prices = historical_data['Close']

# plt.figure(figsize=(10, 6))
# closing_prices.plot(color='blue', linestyle='-')
# plt.title('NASDAQ 100 Closing Prices (Jan 1, 2024 - May 24, 2024)')
# plt.xlabel('Date')
# plt.ylabel('Closing Price')
# plt.grid(True)
# plt.show()
# # plt.figure(figsize=(10, 6))
# # plt.hist(closing_prices, bins=20, color='blue', edgecolor='black')
# # plt.title('Histogram of NASDAQ 100 Closing Prices (Jan 1, 2024 - May 24, 2024)')
# # plt.xlabel('Closing Price')
# # plt.ylabel('Frequency')
# # plt.grid(True)
# # plt.show()


import pandas as pd
import yfinance as yf
import mplfinance as mpf

ticker_symbol = '^IXIC'

historical_data = yf.download(ticker_symbol, start='2024-01-01', end='2024-05-24')

# Convert the index to a DatetimeIndex
historical_data.index = pd.to_datetime(historical_data.index)

# Plot the candlestick chart
mpf.plot(historical_data, type='candle', style='charles', title='NASDAQ 100 Candlestick Chart (Jan 1, 2024 - May 24, 2024)')
