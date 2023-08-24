from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import date
import time
from selenium import webdriver
import sqlite3
import requests
from bs4 import BeautifulSoup

# ChromeDriver 경로를 수동으로 설정합니다.
chrome_driver_path = 'C:/Users/min17/Desktop/증권 백테스팅/chromedriver-win32/chromedriver.exe'

# ChromeDriver 옵션을 설정합니다.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 화면 없는 실행을 원할 경우 주석 해제
chrome_options.add_argument("window-size=1920x1080")

# ChromeDriver를 실행합니다.
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)


'''chrome_options=Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
service=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service, options=chrome_options)

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

chrome_options.add_argument('--headless')'''

driver.implicitly_wait(1)
KosPi_Url='https://finance.daum.net/domestic/after_hours?market=KOSPI'
KosDaq_Url='https://finance.daum.net/domestic/after_hours?market=KOSDAQ'


driver.get(KosPi_Url)

# 종목명 코드
name=[]
for i in range(30):
	nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child("+str(i+1)+") > td:nth-child(1) > a")
	for item in nam:
		nam = item.get_attribute('text')
		name.append(nam)

# 가격 코드
price=[]

pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)

for i in range(1,30):
    pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child("+str(i+1)+") > td:nth-child(2) > span")
    for item in pric:
        pric= item.get_attribute('innerText')
        price.append(pric)

# 체결량 코드
volume=[]

vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
for i in range(1,30):
    vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child("+str(i+1)+") > td.prR > span")
    for item in vol:
        vol= item.get_attribute('innerText')
        volume.append(vol)

#코드 따오기

code=[]
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)

for i in range(1,30):
    cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child("+str(i+1)+") > td:nth-child(1) > a")
    for item in cod:
        cod= str(item.get_attribute("href").split('A')[-1])
        code.append(cod)
# 코스닥 크롤링

driver.get(KosDaq_Url)

driver.implicitly_wait(1)

for i in range(30):
	nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child("+str(i+1)+") > td:nth-child(1) > a")
	for item in nam:
		nam = item.get_attribute('text')
		name.append(nam)

# 가격 코드

pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)

for i in range(1,30):
    pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child("+str(i+1)+") > td:nth-child(2) > span")
    for item in pric:
        pric= item.get_attribute('innerText')
        price.append(pric)

# 체결량 코드

vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
for i in range(1,30):
    vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child("+str(i+1)+") > td.prR > span")
    for item in vol:
        vol= item.get_attribute('innerText')
        volume.append(vol)

#코드 따오기

cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)

for i in range(1,30):
    cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child("+str(i+1)+") > td:nth-child(1) > a")
    for item in cod:
        cod= str(item.get_attribute("href").split('A')[-1])
        code.append(cod)

excp=",'' "

for x in range(len(excp)):
    for i in range(59):
        volume[i]=volume[i].replace(excp[x],"")
for i in range(30):
    volume[i]=int(volume[i])

for x in range(len(excp)):
    for i in range(59):
        price[i]=price[i].replace(excp[x],"")
for i in range(30):
    price[i]=int(price[i])


code_list_end=[]
name_list_end=[]
price_list_end=[]
for i in range(59):
    if int(volume[i])*int(price[i])>3000000000:
        code_list_end.append(code[i])
        name_list_end.append(name[i])
        price_list_end.append(price[i])

print(name_list_end)

driver.quit()

## 크롤링 끝

today=date.today()

# 데이터베이스 추가


conn=sqlite3.connect('Daum_Crawling_list.db',isolation_level=None)

cur=conn.cursor()

code_amount= len(code_list_end)

for i in range(code_amount):
    sql="insert into balance(code, name, bid_price, created_at) values (?,?,?,?)"
    cur.execute(sql, (code_list_end[i],name_list_end[i],price_list_end[i],today))


time.sleep(1)

# 대주가능여부

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


# 대주가능목록 튜플 만들기(리스트는 안만들어서 값은 못뽑음.)

cur.execute('select code from 대주가능목록')
credit_tuple=cur.fetchall()

credit_list=[]

for i in range(a):
    if balance_code[i] in credit_tuple:
        sql="update balance set credit_able=:credit_able where code=:code"
        cur.execute(sql,{"credit_able":"yes","code":balance_code_list[i]})
    else:
        sql = "update balance set credit_able=:credit_able where code=:code"
        cur.execute(sql,{"credit_able":"no","code":balance_code_list[i]})

# SQLite DB 연결
conn = sqlite3.connect('Daum_Crawling_list.db')
cur = conn.cursor()

# balance 테이블에서 종목 코드 가져오기
cur.execute("SELECT code FROM balance")
codes = cur.fetchall()


for code in codes:
    url = f'https://finance.naver.com/item/main.nhn?code={code[0]}'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    price = soup.find('div', {'class': 'today'}).find('span', {'class': 'blind'}).text.replace(',', '')
    cur.execute(f"UPDATE balance SET close = {price} WHERE code = '{code[0]}'")
    conn.commit()


conn.close()
# SQLite 데이터베이스 연결
conn = sqlite3.connect('Daum_Crawling_list.db')

# 커서 생성
cursor = conn.cursor()

# balance 테이블에서 open과 close 열 가져오기
cursor.execute("SELECT bid_price, close FROM balance")
prices = cursor.fetchall()

# 수익률 계산 후 balance 테이블에 입력하기
for price in prices:
    bid_price, close_price = price  # open, close 값 추출
    returns = (close_price - bid_price) / bid_price  # 수익률 계산
    cursor.execute("UPDATE balance SET returns = ? WHERE bid_price = ? AND close = ?", (returns, bid_price, close_price))  # 수익률 입력
    color = 'red' if returns > 0 else 'blue'
    conn.commit()

# 연결 닫기
conn.close()

import sqlite3

# SQLite3 데이터베이스 연결 생성
conn = sqlite3.connect('Daum_Crawling_list.db')
cursor = conn.cursor()

# 최근 10, 20, 40, 80개의 수익률 평균 계산
for n in [10, 20, 40, 60, 80, 100]:
    query = f'SELECT AVG(returns) FROM (SELECT returns FROM balance ORDER BY created_at DESC LIMIT {n})'
    cursor.execute(query)
    avg = cursor.fetchone()[0]
    avg=round(avg,4)
    # AVG_{n} 열에 값 삽입
    query = f'UPDATE balance SET AVG_{n} = {avg*100} WHERE created_at = (SELECT MAX(created_at) FROM balance)'
    cursor.execute(query)

# 데이터베이스 연결 종료
conn.commit()
conn.close()

# SQLite3 데이터베이스에 연결
conn = sqlite3.connect('Daum_Crawling_list.db')
c = conn.cursor()

# credit_able 열에서 yes인 행만 추출하여 평균값 계산
query = 'SELECT AVG(returns) FROM balance WHERE credit_able = "yes";'
c.execute(query)
avg_credit_return = c.fetchone()[0]


# balance 테이블에 credit_return 열 추가하고, 계산된 평균값 삽입

query = f'UPDATE balance SET credit_return = {avg_credit_return * 100} WHERE rowid = (SELECT max(rowid) FROM balance);'
c.execute(query)

# 변경된 내용을 커밋하여 데이터베이스에 반영
conn.commit()

# 연결 종료
conn.close()
