import pandas as pd
import matplotlib.pyplot as plt

# Load the Samsung Electronics stock price data from the 'data/samsung.csv' file into a pandas dataframe
df = pd.read_csv('data/samsung.csv', index_col='날짜', parse_dates=True)

# Create a time series graph with matplotlib
plt.plot(df.index, df['종가'])

# Set the x-axis label to 'Date'
plt.xlabel('Date')

# Set the y-axis label to 'Closing Price'
plt.ylabel('Closing Price')

# Set the title of the graph to 'Samsung Electronics Stock Price'
plt.title('Samsung Electronics Stock Price')

# Show the graph
plt.show()
