import sqlite3

# SQLite3 데이터베이스에 연결
conn = sqlite3.connect('Daum_Crawling_list.db')
cursor = conn.cursor()

# code열에서 중복된 종목코드들을 불러옵니다.
cursor.execute('SELECT code FROM balance GROUP BY code HAVING COUNT(*) > 1')
results = cursor.fetchall()

# 결과 출력
code_list = [result[0] for result in results]
print(code_list)

# 데이터베이스 연결 종료
conn.close()

import pandas as pd
import requests
from bs4 import BeautifulSoup


dfs = {}
for code in code_list:
    url = 'http://fchart.stock.naver.com/sise.nhn?symbol='+code+'&timeframe=day&count=500&requestType=0'
    response = requests.get(url)
    html = BeautifulSoup(response.text, "html")
    item_list = html.find_all('item')
    data_list = []
    for item in item_list:
        data=item['data'].split('|')
        data_list.append(data)
    column_list=['날짜','시가','고가','저가','종가','거래량']
    df=pd.DataFrame(data_list, columns=column_list)
    dfs[code] = df


# 코드를 키로 넣으면 종목정보 데이터 프레임을 출력함.
#ex: print(dfs['005930'])


'''Now you can access each DataFrame using its corresponding stock code as the key

for code, df in dfs.items():
    print(f"DataFrame for {code}:")
    print(df)'''

''' 전체 표준편차
for code, df in dfs.items():
    std = df['거래량'].astype(int).std()
    print(f"Code {code}: 기준 표준편차 = {std}")

10일 표준편차
for code, df in dfs.items():
    recent_df = df[-10:]
    std = recent_df['거래량'].astype(int).std()
    print(f"Code {code}: 10일 표준편차 = {std}")'''

# 120일 표준편차와 10일 표준편차 비교
'''for code, df in dfs.items():
    recent_df = df[-10:]
    overall_df=df[-120:]
    recent_std = recent_df['거래량'].astype(int).std()
    overall_std = overall_df['거래량'].astype(int).std()
    if recent_std < overall_std:
        print(f"Code {code}: recent std = {recent_std:.2f}, overall std = {overall_std:.2f}")
# 거래량 음봉 6일 이상 종목
for code, df in dfs.items():
    recent_df = df[-10:]
    decreased = (recent_df['거래량'].astype(int) < recent_df['거래량'].astype(int).shift(1))
    count = decreased.rolling(window=10).sum().iloc[-1]
    if count >= 6:
        print(f"Code {code}: {count} out of the last 10 days had decreasing 거래량")'''

# 최근 표준편차가 작으면서 거래량 음봉 7일 이상
for code, df in dfs.items():
    recent_df = df[-10:]
    recent_std = recent_df['거래량'].astype(int).std()
    overall_std = df['거래량'].astype(int).std()
    decreased_count = (recent_df['거래량'].astype(int).diff() < 0).sum()
    if recent_std < overall_std and decreased_count >= 7:
        print(f"Code {code}: recent std = {recent_std:.2f}, overall std = {overall_std:.2f}, decreased count = {decreased_count}")