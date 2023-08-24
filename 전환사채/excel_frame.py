import pandas as pd
import sqlite3
from io import BytesIO
import datetime
import requests
from sqlalchemy import create_engine

excel_base='C:/Users/min17/Desktop/증권 백테스팅/전환사채 0623-0820.xls'
sql_base='C:/Users/min17/Desktop/증권 백테스팅/전환사채 0623-0820.db'


#1단계 엑셀 가져오기

# Excel 파일에서 데이터를 읽어옵니다.
df = pd.read_excel(excel_base, header=2)

# SQLite 데이터베이스에 연결합니다.
conn = sqlite3.connect(sql_base)

# 데이터를 'convertible_bond' 테이블에 삽입합니다.
df.to_sql('convertible_bond', conn, if_exists='replace', index=False)

# 변경 사항 커밋
conn.commit()

# 연결 닫기
conn.close()

#2단계 열 설정하기

# SQLite 데이터베이스 연결
conn = sqlite3.connect(sql_base)
cursor = conn.cursor()

# 새로운 테이블 생성
cursor.execute('CREATE TABLE new_table AS SELECT [회사명], [접수일], [사채의 종류(회차)], [사채의 이율(표면이자율 (%))], [사채의 이율(만기이자율 (%))], [사채만기일], [전환에 관한 사항(전환가액 (원/주))], [전환에 관한 사항(전환에 따라 발행할 주식(주식총수 대비 비율(%)))], [전환에 관한 사항(전환청구기간(시작일))], [전환에 관한 사항(전환청구기간(종료일))], [전환에 관한 사항(시가하락에 따른 전환가액 조정(최저 조정가액 (원)))] FROM convertible_bond')
# 원래 테이블 삭제
cursor.execute('DROP TABLE convertible_bond')

# 새로운 테이블 이름 변경
cursor.execute('ALTER TABLE new_table RENAME TO convertible_bond')

# 변경 사항 커밋
conn.commit()

# 연결 닫기
conn.close()


#3단계 코드 업데이트


# SQLite 데이터베이스에 연결
conn = sqlite3.connect(sql_base)

# SQLite에서 pandas로 DataFrame 읽어오기
df_sql = pd.read_sql_query("SELECT * FROM convertible_bond", conn)



# Excel 파일에서 pandas로 DataFrame 읽어오기
df_excel = pd.read_excel('C:/Users/min17/Desktop/증권 백테스팅/증권기본정보.xlsx')

# 필요한 열만 선택
df_excel = df_excel[['code', '회사명']]

# 열 이름을 'code'와 '회사명'으로 변경
df_excel.columns = ['code', '회사명']


# 회사명을 기준으로 두 DataFrame을 병합하기
df_merged = pd.merge(df_sql, df_excel, on='회사명', how='left')

# 병합된 DataFrame을 다시 SQLite에 업데이트
df_merged.to_sql('convertible_bond', conn, if_exists='replace', index=False)

# SQLite 연결 종료
conn.close()

#4단계 시작일시가,시가총액 입력하기

counter=0
# 가격 불러오기 함수
#종가 함수
def get_price_from_krx1(code, date):
    global counter  # declare the global variable 'counter'
    date = datetime.datetime.strptime(date, "%Y%m%d")
    date_str = date.strftime("%Y%m%d")
    gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
    gen_otp_data = {
        'mktId': 'ALL',
        'trdDd': date_str,
        'money': '1',
        'csvxls_isNo': 'false',
        'name': 'fileDown',
        'url': 'dbms/MDC/STAT/standard/MDCSTAT01501'
    }
    headers = {'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader'}
    otp = requests.post(gen_otp_url, gen_otp_data, headers=headers).text
    down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
    down_sector_KS = requests.post(down_url, {'code': otp}, headers=headers)
    data = pd.read_csv(BytesIO(down_sector_KS.content), encoding='EUC-KR')
    # Assuming the column for stock code is '종목코드'
    selected_data = data[data['종목코드'] == code]
    # If the selected_data dataframe is empty (i.e., the stock code was not found)
    counter += 1  # increment the counter
    print(counter)
    if selected_data.empty:
        return None
    return selected_data['종가'].values[0]

#시가총액함수
def get_price_from_krx2(code, date):
    global counter  # declare the global variable 'counter'
    date = datetime.datetime.strptime(date, "%Y%m%d")
    date_str = date.strftime("%Y%m%d")
    gen_otp_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
    gen_otp_data = {
        'mktId': 'ALL',
        'trdDd': date_str,
        'money': '1',
        'csvxls_isNo': 'false',
        'name': 'fileDown',
        'url': 'dbms/MDC/STAT/standard/MDCSTAT01501'
    }
    headers = {'Referer': 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader'}
    otp = requests.post(gen_otp_url, gen_otp_data, headers=headers).text
    down_url = 'http://data.krx.co.kr/comm/fileDn/download_csv/download.cmd'
    down_sector_KS = requests.post(down_url, {'code': otp}, headers=headers)
    data = pd.read_csv(BytesIO(down_sector_KS.content), encoding='EUC-KR')

    # Assuming the column for stock code is '종목코드'
    selected_data = data[data['종목코드'] == code]
    # If the selected_data dataframe is empty (i.e., the stock code was not found)
    counter += 1  # increment the counter
    print(counter)
    if selected_data.empty:
        return None
    return selected_data['시가총액'].values[0]

# SQLite 데이터베이스에 연결
conn = sqlite3.connect(sql_base)

# SQLite에서 pandas로 DataFrame 읽어오기
df = pd.read_sql_query("SELECT * FROM convertible_bond", conn)
# '접수일' 컬럼을 datetime 형식으로 변환

df['접수일'] = df['접수일'].str.replace('년', '').str.replace('월', '').str.replace('일', '').str.replace('-','')

df['시작일시가'] = df.apply(lambda row: get_price_from_krx1(row['code'], row['접수일']), axis=1)
df['시가총액'] = df.apply(lambda row: get_price_from_krx2(row['code'], row['접수일']), axis=1)

# DataFrame을 다시 SQLite에 업데이트합니다.
df.to_sql('convertible_bond', conn, if_exists='replace', index=False)

# SQLite 연결을 종료합니다.
conn.close()

#월별금리 입력하기


# 엑셀 파일에서 날짜와 월별 금리를 불러옵니다.
df_excel = pd.read_excel('C:/Users/min17/Desktop/증권 백테스팅/월별시장금리.xlsx')

# 필요한 열만 선택
df_excel = df_excel[['날짜', '금리']]

# 열 이름을 '날짜'와 '월별금리'로 변경
df_excel.columns = ['날짜', '월별금리']

# Excel에서 날짜와 월별 금리를 딕셔너리로 변환
date_rate_dict = dict(zip(df_excel['날짜'], df_excel['월별금리']))

# SQL 데이터베이스에 연결합니다.
conn = sqlite3.connect(sql_base)

# SQL에서 데이터를 pandas DataFrame으로 읽어옵니다.
df_sql = pd.read_sql_query("SELECT * FROM convertible_bond", conn)

# 월별 금리를 SQL에 추가합니다.
for date_str in df_sql['접수일']:
    # 날짜 형식을 맞춥니다. (예: 20201212 -> 2020년 12월)
    date_obj = pd.to_datetime(date_str, format='%Y%m%d')
    formatted_date = date_obj.strftime('%Y/%m')

    # 해당 날짜와 일치하는 행을 찾아서 월별 금리를 업데이트합니다.
    rate = date_rate_dict.get(formatted_date)
    if rate is not None:
        df_sql.loc[df_sql['접수일'] == date_str, '월별금리'] = rate

# 업데이트된 DataFrame을 SQL에 저장합니다.
df_sql.to_sql('convertible_bond', conn, if_exists='replace', index=False)

# SQL 연결을 종료합니다.
conn.close()

# SQL 데이터베이스에 연결합니다.
conn = sqlite3.connect(sql_base)

# SQL에서 데이터를 pandas DataFrame으로 읽어옵니다.
df_sql = pd.read_sql_query("SELECT * FROM convertible_bond", conn)

# Convert '월별금리' and '표면이자율' columns to numeric, handle non-convertible values as NaN
df_sql['월별금리'] = pd.to_numeric(df_sql['월별금리'], errors='coerce')
df_sql['사채의 이율(표면이자율 (%))'] = pd.to_numeric(df_sql['사채의 이율(표면이자율 (%))'], errors='coerce')

# Calculate the difference and save in the '금리차' column
df_sql['금리차'] = df_sql['월별금리'] - df_sql['사채의 이율(표면이자율 (%))']

# 업데이트된 DataFrame을 SQL에 저장합니다.
df_sql.to_sql('convertible_bond', conn, if_exists='replace', index=False)

# SQL 연결을 종료합니다.
conn.close()

# 마지막 정리된 데이터 삽입하기

sql_base='C:/Users/min17/Desktop/증권 백테스팅/전환사채 0623-0820.db'
source_conn = sqlite3.connect(sql_base)
source_cursor = source_conn.cursor()

source_cursor.execute('SELECT * FROM convertible_bond')
data_to_copy = source_cursor.fetchall()

source_conn.close()

target_conn = sqlite3.connect('C:/Users/min17/Desktop/증권 백테스팅/전환사채 목록2(금리추가).db')
target_cursor = target_conn.cursor()

for row in data_to_copy:
    new_row = list(row) + [None] * (24 - len(row))
    target_cursor.execute('INSERT INTO convertible_bond VALUES (?, ?, ?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?, ?,?,?) ', new_row)

target_conn.commit()
target_conn.close()

