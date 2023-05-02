import pandas as pd
import FinanceDataReader as fdr

start_date='2015-01-01'
end_date='2023-04-29'

# 나스닥 지수 데이터 가져오기

nasdaq = fdr.DataReader('IXIC', start_date, end_date)

# 코스닥 종합 지수 데이터 가져오기
kosdaq = fdr.DataReader('KS11', start_date, end_date)

# 나스닥 하락 다음 날 코스닥 시가로 매수, 10일 후/20일 후 종가로 매도
trade_dates = nasdaq[(nasdaq['Close'].pct_change() > 0.02)].index
results = []
for date in trade_dates:
    if date.weekday() not in [0, 1, 2, 3]:
        continue # 화,수,목만 처리
    next_date = date + pd.Timedelta(days=1)
    try:
        kosdaq_data = kosdaq.loc[str(next_date)]
    except KeyError:
        continue
    if kosdaq_data.empty:
        continue # 데이터가 없으면 건너뜀
    buy_price = kosdaq_data['Open']
    try:
        sell_price_7 = kosdaq.loc[str(next_date + pd.Timedelta(days=7))]['Close']
    except KeyError:
        continue
    try:
        sell_price_14 = kosdaq.loc[str(next_date + pd.Timedelta(days=14))]['Close']
    except:
        continue
    profit_7 = (sell_price_7 - buy_price) / buy_price * 100
    profit_14 = (sell_price_14 - buy_price) / buy_price * 100
    results.append([next_date, profit_7, profit_14])

# 결과 출력
results_df = pd.DataFrame(results, columns=['Date', 'Profit(7d)', 'Profit(14d)'])
print(results_df)
mean_profit7d=results_df['Profit(7d)'].mean()
mean_profit14d=results_df['Profit(14d)'].mean()
print('Mean Profit(7d): {:.2f}%'.format(mean_profit7d))
print('Mean Profit(14d): {:.2f}%'.format(mean_profit14d))