import math

import requests
from bs4 import BeautifulSoup
import numpy as np
from datetime import datetime
from api.Kiwoom import *
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import date


chrome_options=Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
service=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service, options=chrome_options)

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

chrome_options.add_argument('--headless')

driver.implicitly_wait(1)
KosPi_Url='https://finance.daum.net/domestic/after_hours?market=KOSPI'
KosDaq_Url='https://finance.daum.net/domestic/after_hours?market=KOSDAQ'


driver.get(KosPi_Url)

# 종목명 코드
name=[]
#for i in range (1,30):
#    nam=driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(1) > a")
#    for item in nam:
#        namm = item.get_attribute('text')
#        print(namm)
#        name.append(namm)
#    print(name)


nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(1) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)

nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(6) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(7) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)

nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(8) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(9) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(10) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(11) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(12) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(13) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(14) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(15) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(16) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(17) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(18) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(19) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(20) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(21) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(22) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)

nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(23) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(24) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(25) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(26) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(27) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(28) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(29) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(30) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)


                                                        # 가격 코드
price=[]

pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(6) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(7) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(8) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(9) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(10) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(11) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(12) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(13) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(14) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(15) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(16) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(17) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(18) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(19) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(20) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(21) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(22) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(23) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(24) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(25) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(26) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(27) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(28) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(29) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(30) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)

# 체결량 코드
volume=[]

vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(6) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(7) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(8) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(9) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(10) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(11) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(12) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(13) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(14) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(15) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(16) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(17) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(18) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(19) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(20) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(21) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(22) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(23) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(24) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(25) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(26) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(27) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(28) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(29) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(30) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)



#코드 따오기

code=[]
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(6) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(7) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(8) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(9) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(10) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(11) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(12) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(13) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(14) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(15) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(16) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(17) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(18) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(19) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(20) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(21) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(22) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(23) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(24) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(25) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(26) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(27) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(28) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(29) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(30) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)


# 코스닥 크롤링

driver.get(KosDaq_Url)

driver.implicitly_wait(1)

nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(6) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(7) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)

nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(8) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(9) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(10) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(11) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(12) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(13) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(14) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(15) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(16) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(17) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(18) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(19) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(20) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(21) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(22) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)

nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(23) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(24) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(25) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(26) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(27) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(28) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(29) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)
nam= driver.find_elements(By.CSS_SELECTOR, "#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(30) > td:nth-child(1) > a")
for item in nam:
        nam = item.get_attribute('text')
        name.append(nam)

# 가격

pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(6) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(7) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(8) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(9) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(10) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(11) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(12) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(13) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(14) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(15) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(16) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(17) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(18) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(19) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(20) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(21) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(22) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(23) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(24) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(25) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(26) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(27) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(28) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(29) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)
pric= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(30) > td:nth-child(2) > span")
for item in pric:
    pric= item.get_attribute('innerText')
    price.append(pric)

#거래량

vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(5) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(6) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(7) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(8) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(9) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(10) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(11) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(12) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(13) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(14) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(15) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(16) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(17) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(18) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(19) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(20) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(21) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(22) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(23) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(24) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(25) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(26) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(27) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(28) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(29) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)
vol= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(30) > td.prR > span")
for item in vol:
    vol= item.get_attribute('innerText')
    volume.append(vol)

cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr.first > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(2) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(4) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(6) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(7) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(8) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(9) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(10) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(11) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(12) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(13) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(14) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(15) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(16) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(17) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(18) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(19) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(20) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(21) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(22) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(23) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(24) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(25) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(26) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(27) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(28) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(29) > td:nth-child(1) > a")
for item in cod:
    cod= str(item.get_attribute("href").split('A')[-1])
    code.append(cod)
cod= driver.find_elements(By.CSS_SELECTOR,"#boxAfterHours > div.box_contents > div:nth-child(1) > table > tbody > tr:nth-child(30) > td:nth-child(1) > a")
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
for i in range(59):
    price[i]=int(price[i])


code_list_end=[]
name_list_end=[]
price_list_end=[]
for i in range(59):
    if int(volume[i])*int(price[i])>2000000000:
        code_list_end.append(code[i])
        name_list_end.append(name[i])
        price_list_end.append(price[i])

print(name_list_end)

driver.quit()

## 크롤링 끝

today=date.today()

code_amount= len(code_list_end)


now= datetime.now()
before_start=now.replace(hour=8, minute=25, second=0, microsecond=0)
start_time1= now.replace(hour=8, minute=40, second=0, microsecond=0)
start_time2= now.replace(hour=9, minute=0, second=0, microsecond=0)
cancel_time1=now.replace(hour=9, minute=0, second=0, microsecond=0)
cancel_time2=now.replace(hour=9, minute=2, second=0, microsecond=0)
end_time1=now.replace(hour=9, minute=3, second=0, microsecond=0)
end_time2=now.replace(hour=9, minute=20, second=0, microsecond=0)


app= QApplication(sys.argv)
kiwoom=Kiwoom()


budget= 1000000/code_amount

#장전주문

if before_start<=now<=start_time1:
    for i in range(code_amount):
        bid = price_list_end[i]
        quantity=math.floor(budget / bid)
        order_result=kiwoom.send_order('send_buy_order','0110',1,code_list_end[i], quantity, 0,'61')
        print(order_result)

#동시호가 주문

#if start_time1<=now<=start_time2:
#    for i in range(code_amount):
#        bid=price_list_end[i]
#        quantity=math.floor(budget/bid)
#        order_result= kiwoom.send_order('send_buy_order', '1001', 1, code_list_end[i], quantity, price_list_end[i], '00')
#        print(order_result)



app.exec_()
