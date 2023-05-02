import pandas as pd
import FinanceDataReader as fdr

# 나스닥 2퍼 이상 상승할 때 코스닥 매수, 매도 함수
def calculate_positive(start_date, end_date):
    # 나스닥 지수 데이터 가져오기
    nasdaq = fdr.DataReader('IXIC', start_date, end_date)

    # 2% 이상 하락한 날짜 필터링
    nasdaq_down = nasdaq[(nasdaq['Close'].pct_change() > 0.02)]

    # 코스닥 종합 지수 데이터 가져오기
    kosdaq = fdr.DataReader('KS11', start_date, end_date)

    # 나스닥 하락 다음 날 코스닥 시가로 매수, 종가로 매도
    profit_list = []
    trade_dates = nasdaq_down.index.date
    traded_dates = []
    cumulative_return = 1
    for date in trade_dates:
        if date.weekday() not in [0, 1, 2, 3]:
            continue  # 화수목금만 처리
        try:
            # 나스닥 하락 다음 날의 코스닥 데이터 가져오기
            kosdaq_data = kosdaq.loc[str(date + pd.Timedelta(days=1))]
        except KeyError:  # KeyError 예외 처리
            continue  # 데이터가 없으면 건너뜀
        if kosdaq_data.empty:
            continue  # 데이터가 없으면 건너뜀
        buy_price = kosdaq_data['Open']
        sell_price = kosdaq_data['Close']
        profit = (sell_price - buy_price) / buy_price * 100
        cumulative_return *= 1 + profit / 100
        profit_list.append(profit)
        traded_dates.append(str(date + pd.Timedelta(days=1)))
        # cumulative_return 갱신
        if not pd.isna(profit):
            cumulative_return *= 1 + profit / 100

    # 결과 출력

    result = pd.DataFrame({'Date': traded_dates, 'Profit(%)': profit_list})
    print(result)
    mean_profit = result['Profit(%)'].mean()
    print('Mean Profit: {:.2f}%'.format(mean_profit))

    return mean_profit

# 나스닥 2퍼 이상 하락할 때 코스닥 매수, 매도 함수

def calculate_negative(start_date, end_date):
    # 나스닥 지수 데이터 가져오기
    nasdaq = fdr.DataReader('IXIC', start_date, end_date)

    # 2% 이상 하락한 날짜 필터링
    nasdaq_down = nasdaq[(nasdaq['Close'].pct_change() < -0.02)]

    # 코스닥 종합 지수 데이터 가져오기
    kosdaq = fdr.DataReader('KS11', start_date, end_date)

    # 나스닥 하락 다음 날 코스닥 시가로 매수, 종가로 매도
    profit_list = []
    trade_dates = nasdaq_down.index.date
    traded_dates = []
    cumulative_return = 1
    for date in trade_dates:
        if date.weekday() not in [0, 1, 2, 3]:
            continue  # 화수목금만 처리
        try:
            # 나스닥 하락 다음 날의 코스닥 데이터 가져오기
            kosdaq_data = kosdaq.loc[str(date + pd.Timedelta(days=1))]
        except KeyError:  # KeyError 예외 처리
            continue  # 데이터가 없으면 건너뜀
        if kosdaq_data.empty:
            continue  # 데이터가 없으면 건너뜀
        buy_price = kosdaq_data['Open']
        sell_price = kosdaq_data['Close']
        profit = (sell_price - buy_price) / buy_price * 100
        cumulative_return *= 1 + profit / 100
        profit_list.append(profit)
        traded_dates.append(str(date + pd.Timedelta(days=1)))
        # cumulative_return 갱신
        if not pd.isna(profit):
            cumulative_return *= 1 + profit / 100

    # 결과 출력

    result = pd.DataFrame({'Date': traded_dates, 'Profit(%)': profit_list})
    print(result)
    mean_profit = result['Profit(%)'].mean()
    print('Mean Profit: {:.2f}%'.format(mean_profit))

    return mean_profit


calculate_positive('2020-01-01','2023-01-01' )
