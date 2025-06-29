import json
import requests
import pandas as pd
from datetime import date
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# API - to fetch temperature of a city
# city_name = input('Enter a City name: ')
# app.config['API_KEY'] = os.getenv('API_KEY')

# Building our API to fetch our data
# api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

# api_url = 'https://api.openweathermap.org/data/2.5/weather'

# params = {
#     'q': 'Lagos',
#     'api_key': app.config['API_KEY'],
#     'units': 'metric'
# }

# Make request to the api url for some data
# response = requests.get(api_url, params=params)
# data = response.json()

# df = pd.DataFrame(data['weather'])
# df = pd.json_normalize(data, record_path)
# df = pd.read_json(data)

# print(df)
# print(response.headers)
# print(response.url)
# print(response.status_code)
# print(response.encoding)
# print(response.headers['Content-Type'])
# print(response.headers['Content-Length'])
# print(response.text[0:100])
# print(response.json())
# print(response.status_code)
# data = response.json()
# print(data)


# response = {
#     "weather": [
#     {
#       "id": 801,
#       "main": "Clouds",
#       "description": "few clouds",
#       "icon": "02n"
#     }
#   ]
# }

# result = response["weather"][0]["main"]
# print(result)

# Coinmarketcap API
root_url = "https://api.coingecko.com/api/v3"
# endpoint = "/ping" # returns '{"gecko_says":"(V3) To the Moon!"}'
# endpoint = "/coins/list" # used to retrieve the coins list
uid = 'bitcoin'
# endpoint = "/coins/markets"
 # Used to obtain all the coins market data (price, market cap, volume)
endpoint = f'/coins/{uid}/market_chart'
params = {
    'vs_currency': 'usd',
    # 'id': 'bitcoin'
    'days': '1'
}
response = requests.get(root_url+endpoint, params=params)
data = response.json()
# Converting to a DataFrame
df = pd.DataFrame(data)
df = pd.json_normalize(response.json())
# df = df.reset_index() # to change the indexing of the data
# df = df.rename(columns={'index': 'symbol'}) # renames the index column in the dataframe
print(df['prices'].str[0])
#adding a timestamp column
#str[0] extracts the first character from each price string in the prices column
df['timestamp'] = df['prices'].str[0]
df['prices'] = df['prices'].str[1]
df['market_caps'] = df['market_caps'].str[1]
df['total_volumes'] = df['total_volumes'].str[1]
# Rearranging the dataframe
df = df[['timestamp', 'prices', 'market_caps', 'total_volumes']]
df = pd.to_datetime(df['timestamp'], unit='ms')
print(df.describe) # To obtain more information on the dataframe
print(df.info)
print(df)
print(df.head())
# print(df.head())
# print(df)
# print(df.head)
# print(df.shape)
# print(df.loc[(df.id=='bitcoin') | (df.id=='ethereum') | (df.id=='dogecoin')])
# print(data.keys())
# print(response.headers)
# print(response.status_code)

# Retrieve today's date
today = date.today().strftime('%d/%m/%Y')
# uid = 'bitcoin'
# root_url = 'https://api.coingecko.com/api/v3'
# endpoint = f'/coins/{uid}/history'
# params = {
#     'date': today
# }
# response = requests.get(root_url+endpoint, params=params)
# data = response.json()
# print(data)
# print(response.status_code)
# print('Today:', today)

# Storing the data in a dataframe
# url = f'https://api.coingecko.com/api/v3/coins/bitcoin/history?date={today}'
# df = pd.read_json(url)
# print(df.head())

# Saving the data in a json file
# file_name = f'bitcoin_history_{today}.json'
# with open(file_name, 'w') as f:
#     json.dump(data, f)
# print(data.keys())


    
