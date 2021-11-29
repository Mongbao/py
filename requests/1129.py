from datetime import datetime
import requests
import sqlite3
 
 
response = requests.get(
    f'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20211129&stockNo=2330&_=1638183876155')
response_data = response.json()['data']
 
print(response_data)