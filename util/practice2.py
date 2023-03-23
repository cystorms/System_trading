import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/item/sise_day.nhn?code=005930'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

volume_list = []
trs = soup.select('#content > table > tr')[1:11]
for tr in trs:
    volume = tr.select('span')[6].text.strip().replace(',', '')
    volume_list.append(volume)

print(f"종목코드: 005930, 거래량: {volume_list}")