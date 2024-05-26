import yfinance as yf
import pandas as pd

# The icker symbol for NASDAQ 100
ticker_symbol = '^IXIC'
# historical prices from January 1, 2024, to May 24, 2024
historical_data = yf.Ticker(ticker_symbol).history( start='2024-01-01', end='2024-05-24', )

# Display the first few rows of the data
print(historical_data.head())

# Save the data to a CSV file
historical_data.to_csv('NAS100_2024.csv')
