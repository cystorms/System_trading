import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from datetime import datetime

import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

BASE_URL='https://finance.naver.com/sise/sise_market_sum.nhn?sosok='
CODES=[0,1]
START_PAGE=1
fields=[]

now=datetime.now()
formattedDate=now.strftime("%Y%m%d")

chrome_options=Options()
chrome_options.add_experimental_option("detach", True)

chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
service=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service, options=chrome_options)


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

chrome_options.add_argument('headless')

driver.implicitly_wait(1)

def execute_crawler():
    df_total=[]

    for code in CODES:
        res = requests.get(BASE_URL + str(CODES[0]))
        page_soup=BeautifulSoup(res.text, 'lxml')
        total_page_num=page_soup.select_one('td.pgRR>a')

        total_page_num = int(total_page_num.get('href').split('=')[-1])

        ipt_html = page_soup.select_one('div.subcnt_sise_item_top')
        global fields
        fields = [item.get('value') for item in ipt_html.select('input')]
        result=[crawler(code, str(page)) for page in range(1, total_page_num+1)]

        df=pd.concat(result, axis=0, ignore_index=True)
        df_total.append(df)

    df_total=pd.concat(df_total)
    df_total.reset_index(inplace=True, drop=True)
    df_total.to_excel('NaverFinance.xlsx')
    return df_total

def crawler(code, page):
    global fields
    data={'menu':'market_sum','fieldIds': fields, 'returnUrl':BASE_URL+str(code)+"&page=" + str(page)}

    res=requests.post('http://finance.naver.com/sise/field_submit.nhn', data=data)
    page_soup=BeautifulSoup(res.text, 'lxml')
    table_html= page_soup.select_one('div.box_type_l')
    print(table_html)
    header_data=[item.get_text().strip() for item in table_html.select('thead tr')]
    inner_data=[item.get_text().strip() for item in table_html.find_all(lambda x:
                                                                        (x.name=='a'and
                                                                         'title' in x.get('class',[])) or
                                                                        (x.name == 'td' and 'number' in x.get('class',[])))]
    no_data=[item.get_text().strip() for item in table_html.select('td.no')]
    number_data= np.array(inner_data)
    number_data.resize(len(no_data), len(header_data))
    df=pd.DataFrame(data=number_data, columns=header_data)
    return df


if __name__=="__main__":
    print('Start!')
    execute_crawler()
    print('End')