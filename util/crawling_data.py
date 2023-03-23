import numpy as np
from datetime import datetime
from api.Kiwoom import *
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

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
KosPi_Url='https://finance.daum.net/domestic/after_hours?market=KOSPI'
KosDaq_Url='https://finance.daum.net/domestic/after_hours?market=KOSDAQ'

def execute_crawler():
    df_total = []