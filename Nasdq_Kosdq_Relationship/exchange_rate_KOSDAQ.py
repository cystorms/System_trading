import pandas as pd
import FinanceDataReader as fdr
import matplotlib.pyplot as plt

# 환율 데이터 불러오기
exchange_rate = fdr.DataReader('USD/KRW', '2021-01-01', '2023-04-30')

# 코스닥 데이터 불러오기
kosdaq = fdr.DataReader('KOSDAQ', '2021-01-01', '2023-04-30')

# 날짜(date)를 기준으로 두 데이터를 합치기
data = pd.merge(exchange_rate, kosdaq, on='Date')

# 그래프 그리기
fig, ax1 = plt.subplots()

ax1.plot(data['Date'], data['USD/KRW'], color='red')
ax1.set_ylabel('Exchange Rate (USD/KRW)', color='red')

ax2 = ax1.twinx()
ax2.plot(data['Date'], data['Close'], color='blue')
ax2.set_ylabel('KOSDAQ', color='blue')

plt.show()