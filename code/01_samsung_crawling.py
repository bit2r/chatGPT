import requests
import pandas as pd

# URL of Samsung Electronics stock historical data
url = "https://finance.naver.com/item/sise_day.naver?code=005930&page="

# Empty list to store stock price data
data = []

# Loop through the last 3 years of pages (60 pages in total)
for page in range(1, 61):
    # Send a GET request to the URL with the current page number
    response = requests.get(url + str(page), headers={'User-agent': 'Mozilla/5.0'})
    

    # Check if the response is successful
    if response.status_code == 200:
        # Read the HTML table into a pandas dataframe
        df_list = pd.read_html(response.text, flavor='html5lib')

        # Check if the list of dataframes is not empty
        if df_list:
            # Get the first dataframe
            df = df_list[0]

            # Drop the last row which is just a duplicate of the column headers
            df = df.drop(len(df) - 1)

            # Append the dataframe to the list
            data.append(df)

# Concatenate all dataframes into a single dataframe
df = pd.concat(data)

# Reverse the order of rows to start from the earliest date
df = df.iloc[::-1]

df = df.dropna()

# Set the date column as the index and remove unnecessary columns
df = df.set_index('날짜')[['종가', '거래량']]

# Convert the data types of columns to float and int
df['종가'] = df['종가'].astype(float)
df['거래량'] = df['거래량'].astype(int)

# Save the dataframe as a CSV file
df.to_csv('data/samsung.csv')

# Print a confirmation message
print('samsung.csv saved successfully.')


