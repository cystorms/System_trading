import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'http://fchart.stock.naver.com/sise.nhn?symbol=066570&timeframe=day&count=500&requestType=0'
response = requests.get(url)
html=BeautifulSoup(response.text,"html")
item_list=html.find_all('item')

data_list=[]
for item in item_list:
    data=item['data'].split('|')
    data_list.append(data)
    column_list=['날짜','시가','고가','저가','종가','거래량']
    day_price_df=pd.DataFrame(data_list, columns=column_list)
    print(day_price_df)