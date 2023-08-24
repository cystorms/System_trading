import pandas as pd
import sqlite3

# SQLite 데이터베이스에 연결
conn = sqlite3.connect('C:/Users/min17/Desktop/증권 백테스팅/전환사채 목록2(금리추가).db')

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
