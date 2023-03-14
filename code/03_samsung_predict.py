import pandas as pd
import pmdarima as pm
import numpy as np

# Load the Samsung Electronics stock price data from the 'data/samsung.csv' file into a pandas dataframe
data = pd.read_csv('data/samsung.csv', index_col='날짜', parse_dates=True)

data.dtypes

# Extract the '종가' column and leave it as dataframe
closing_prices = data[['종가']]

# Create an ARIMA model using pmdarima
stepwise_model = pm.auto_arima(closing_prices, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)

print(stepwise_model.aic())

# data.index.min(), # data.index.max()

# Make a prediction for the next 30 days
future_dates = pd.date_range(start='2023-03-15', end='2023-04-14')
future_forecast = stepwise_model.predict(n_periods = len(future_dates))

# Create a DataFrame of forecasted values with future dates as the index
forecast_df = pd.DataFrame({'종가': future_forecast,
                            '날짜': future_dates})
                            
forecast_df.set_index('날짜', inplace=True)

# Print the forecasted values
full_df = pd.concat([closing_prices, forecast_df], axis = 0)

print(full_df)

full_df.to_csv("data/samsung_forecast.csv")
