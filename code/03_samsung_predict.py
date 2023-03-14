import pandas as pd
import pmdarima as pm

# Load the Samsung Electronics stock price data from the 'data/samsung.csv' file into a pandas dataframe
data = pd.read_csv('data/samsung.csv', index_col='날짜', parse_dates=True)

# Extract the '종가' column as a pandas series
closing_prices = data['종가']

# Create an ARIMA model using pmdarima
stepwise_model = pm.auto_arima(closing_prices, start_p=1, start_q=1,
                           max_p=3, max_q=3, m=12,
                           start_P=0, seasonal=True,
                           d=1, D=1, trace=True,
                           error_action='ignore',  
                           suppress_warnings=True, 
                           stepwise=True)

print(stepwise_model.aic())

# 데이터 
train = data.loc['1985-01-01':'2016-12-01']
test = data.loc['2017-01-01':]

# Make a prediction for the next 30 days
df['forecast'] = pd.DataFrame(model.predict(n_periods=30), index = df.index,
                              columns=[‘Prediction’])

# Create a new column in the dataframe to store the predicted prices
df['Predicted Price'] = None

# Calculate the predicted prices for the next 30 days
last_price = closing_prices[-1]
for i in range(30):
    predicted_price = last_price * (1 + forecast[i])
    date = closing_prices.index[-1] + pd.DateOffset(days=i+1)
    df.at[date, 'Predicted Price'] = predicted_price

# Print the dataframe with the predicted prices
print(df)
