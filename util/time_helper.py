import FinanceDataReader as fdr
import pandas as pd
from datetime import datetime, timedelta
import sqlite3
from datetime import time
# 오늘 날짜 구하기
now= datetime.now()
today = datetime.today().strftime("%Y-%m-%d")
yesterday= now-timedelta(days=1)
yesterday=yesterday.strftime("%Y-%m-%d")

conn=sqlite3.connect('Daum_Crawling_list.db',isolation_level=None)

cur=conn.cursor()

cur.execute('select code from balance')
# balance 코드 뽑기
balance_code=cur.fetchall()

balance_code_list=[]
a=len(balance_code)

# balance 코드 리스트 만들기
for i in range(a):
    row=balance_code[i]
    row=list(row)
    row=row[0]
    balance_code_list.append(row)

# 코스피, 코스닥 종목 코드 불러오기
kospi = fdr.StockListing('KOSPI')
kosdaq = fdr.StockListing('KOSDAQ')



start_time=now.replace(hour=8, minute=25, second=0, microsecond=0)
end_time=now.replace(hour=23, minute=59, second=0, microsecond=0)

# 모든 코스피, 코스닥 종목의 종가 가져오기
close_prices = []
if start_time<now<end_time:
    for code in kospi['Code'].append(kosdaq['Code']):
        # 종목 코드를 사용하여 종가 데이터 가져오기
        df = fdr.DataReader(code, today, today)
        # 종가 데이터 정리하기
        close_price = df['Close'][0]
        # 종가 데이터 리스트에 추가하기
        close_prices.append(close_price)

if now<start_time:
    for code in kospi['Code'].append(kosdaq['Code']):
        # 종목 코드를 사용하여 종가 데이터 가져오기
        df = fdr.DataReader(code, yesterday, yesterday)
        # 종가 데이터 정리하기
        close_price = df['Close'][0]
        # 종가 데이터 리스트에 추가하기
        close_prices.append(close_price)

# 데이터프레임 생성하기
close_df = pd.DataFrame({'Name': kospi['Name'].append(kosdaq['Name']), 'Code': kospi['Code'].append(kosdaq['Code']), 'Close': close_prices})

# 결과 출력하기
print(close_df)


conn=sqlite3.connect('Daum_Crawling_list.db',isolation_level=None)

cur=conn.cursor()

for index, row in close_df.iterrows():
    codes=int(row['Code'])
    closes=int(row['Close'])
    print(codes)

    sql="select code from balance where code=:code"
    cursor = conn.cursor()
    cursor.execute(sql, {"code": codes})
    count = cursor.fetchone()[0]

    if count>0:
        sql = "UPDATE balance SET close=:close WHERE code=:code"
        cursor.execute(sql,{"close": closes, "code": codes})
        conn.commit()

