import requests
import json
import datetime
from dateutil.relativedelta import relativedelta

# DART Open API 인증키
api_key = "dad223eb446ae73419026f15c1593dcaab4bf35c"

# DART Open API 엔드포인트 URL
url = f"https://opendart.fss.or.kr/api/list.json?crtfc_key={api_key}&bgn_de=20200101&end_de=20200102&corp_cls=Y&page_no=1&page_count=10&sort=date"
# 시작 날짜
start_date = datetime.datetime(2020, 1, 1)

# 오늘 날짜
end_date = datetime.datetime.now()

# 1달 주기로 데이터 출력
current_date = start_date

while current_date <= end_date:
    # 현재 날짜를 기준으로 30일 후 계산
    next_date = current_date + relativedelta(months=1)

    # 현재 날짜와 30일 후 날짜를 API 호출에 사용
    url = f"https://opendart.fss.or.kr/api/list.json?crtfc_key={api_key}&bgn_de={current_date.strftime('%Y%m%d')}&end_de={next_date.strftime('%Y%m%d')}&corp_cls=Y&page_no=1&page_count=10&sort=date"
    response = requests.get(url)
    data = json.loads(response.text)

    # 전환사채권 발행결정 정보 출력
    result = data.get("list")
    if result:
        if isinstance(result, dict):
            result = [result]  # 단일 데이터인 경우 리스트로 변환

        for item in result:
            rcept_no = item.get("rcept_no")  # 접수번호
            corp_name = item.get("corp_name")  # 기업명
            report_nm = item.get("report_nm")  # 공시명칭
            report_dt = item.get("rcept_dt")  # 공시일자

            print(f"접수번호: {rcept_no}")
            print(f"기업명: {corp_name}")
            print(f"공시명칭: {report_nm}")
            print(f"공시일자: {report_dt}")
            print("------------------------------------")
    else:
        print("데이터를 가져오지 못했습니다.")

    # 다음 주기로 이동
    current_date = next_date