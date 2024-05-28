import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from matplotlib.patches import Rectangle



# Load the existing dataset
file_path = 'NAs100_2024.csv'
data = pd.read_csv(file_path)

# Parse 'Date' column with timezone information and set as index
data['Date'] = pd.to_datetime(data['Date'], utc=True)
data.set_index('Date', inplace=True)

# Save the dataset again to ensure correct format
data.to_csv('NAs100_2024.csv')

def detect_fvg(data):
    fvg_data = []
    for i in range(2, len(data)):
        if data['High'].iloc[i-1] > data['Low'].iloc[i-2] and data['Low'].iloc[i] < data['High'].iloc[i-1]:
            fvg_data.append({
                'start': data.index[i-2],
                'end': data.index[i],
                'fvg_open': data['High'].iloc[i-1],
                'fvg_close': data['Low'].iloc[i-2]
            })
    return fvg_data

def plot_fvg(data, fvg_data):
    fig, axlist = mpf.plot(data, type='candle', returnfig=True)

    for ax in axlist:
        if ax.get_ylabel() == 'Price':
            for fvg in fvg_data:
                rect = Rectangle(
                    (date2num(fvg['start']), fvg['fvg_close']),
                    date2num(fvg['end']) - date2num(fvg['start']),
                    fvg['fvg_open'] - fvg['fvg_close'],
                    linewidth=1, edgecolor='g', facecolor='none'
                )
                ax.add_patch(rect)

    plt.show()

# Read the corrected CSV file
corrected_file_path = 'NAs100_2024.csv'
data = pd.read_csv(corrected_file_path, parse_dates=['Date'], index_col='Date')

# Ensure the index is a DatetimeIndex and localized to UTC if not already
if not isinstance(data.index, pd.DatetimeIndex):
    data.index = pd.to_datetime(data.index)

if data.index.tz is None:
    data.index = data.index.tz_localize('UTC')
else:
    data.index = data.index.tz_convert('UTC')

# Print to debug the index type
print("Index type:")
print(type(data.index))

# Detect fair value gaps
fvg_data = detect_fvg(data)

# Plot the candlestick chart with fair value gaps
plot_fvg(data, fvg_data)
