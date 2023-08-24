
import datetime
start_date = datetime.datetime(2020, 1, 1)
# 시작 날짜
start_date = datetime.datetime(2020, 1, 1)

# 오늘 날짜
end_date = datetime.datetime.now()

# 1달 주기로 데이터 출력
current_date = start_date
print(current_date.strftime('%Y%m%d'))