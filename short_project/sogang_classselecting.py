import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





for i in range(100):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)


    def set_chrome_driver():
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver


    chrome_options.add_argument('headless')

    driver.implicitly_wait(0.5)

    KosPi_Url = 'http://sis109.sogang.ac.kr/sap/bc/bsp/sap/zcm001/default.htm'
    driver.get(KosPi_Url)

#학번 입력!!
    user_id = '20201257'
    user_pw = 'min170300@'

    elem = driver.find_element(By.NAME, 'sap-user')
    elem.clear()
    elem.send_keys(user_id)

    elem = driver.find_element(By.NAME,'sap-password')
    elem.clear()
    elem.send_keys(user_pw)


    # 로그인 버튼 클릭
    driver.find_element(By.XPATH,'//*[@id="main_box"]/tbody/tr[3]/td[2]/a/img').click()

    # 새 창이 나타날 때까지 기다리기

    # 새 창으로 전환하기
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(1)
    # 새 창에서 필요한 작업 수행
    driver.find_element(By.XPATH,'//*[@id="WDDC"]').click()

    driver.find_element(By.XPATH,'//*[@id="WD01E9-r"]').click()

#신청하고 싶은 과목명 입력!!
    driver.find_element(By.XPATH, '//*[@id="WD01E9"]').send_keys('기초인공지능')

    #검색 눌리기
    driver.find_element(By.XPATH,'//*[@id="WDE5"]').click()

#몇번째 과목인지 선택!!
    driver.find_element(By.XPATH, '//*[@id="WD02B9-text"]').click()

    driver.close()

    driver.quit()

    time.sleep(0.5)

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)


    def set_chrome_driver():
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        return driver


    chrome_options.add_argument('headless')

    driver.implicitly_wait(0.5)

    KosPi_Url = 'http://sis109.sogang.ac.kr/sap/bc/bsp/sap/zcm001/default.htm'
    driver.get(KosPi_Url)

#학번 입력!!
    user_id = '20201257'
    user_pw = 'min170300@'

    elem = driver.find_element(By.NAME, 'sap-user')
    elem.clear()
    elem.send_keys(user_id)

    elem = driver.find_element(By.NAME,'sap-password')
    elem.clear()
    elem.send_keys(user_pw)


    # 로그인 버튼 클릭
    driver.find_element(By.XPATH,'//*[@id="main_box"]/tbody/tr[3]/td[2]/a/img').click()

    # 새 창이 나타날 때까지 기다리기

    # 새 창으로 전환하기
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(1)
    # 새 창에서 필요한 작업 수행
    driver.find_element(By.XPATH,'//*[@id="WDDC"]').click()

    driver.find_element(By.XPATH,'//*[@id="WD01E9-r"]').click()

#신청하고 싶은 과목명 입력!!
    driver.find_element(By.XPATH, '//*[@id="WD01E9"]').send_keys('기초인공지능')

    #검색 눌리기
    driver.find_element(By.XPATH,'//*[@id="WDE5"]').click()

#몇번째 과목인지 선택!!
    driver.find_element(By.XPATH, '//*[@id="WD02E5-text"]').click()

    time.sleep(0.5)

    driver.close()

    driver.quit()




