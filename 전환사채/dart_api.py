from bs4 import BeautifulSoup
import requests
import pandas as pd
import io
import zipfile
import xml.etree.ElementTree as et
import json
crtfc_key="dad223eb446ae73419026f15c1593dcaab4bf35c"

def get_corpcode(crtfc_key):
    """
    OpenDART 기업 고유번호 받아오기
    return 값: 주식코드를 가진 업체의 DataFrame
    """
    params = {'crtfc_key':crtfc_key}
    items = ["corp_code","corp_name","stock_code","modify_date"]
    item_names = ["고유번호","회사명","종목코드","수정일"]
    url = "https://opendart.fss.or.kr/api/corpCode.xml" #요청 url
    res = requests.get(url,params=params) #url 불러오기
    zfile = zipfile.ZipFile(io.BytesIO(res.content))  #zip file 받기
    fin = zfile.open(zfile.namelist()[0])  #zip file 열고
    root = et.fromstring(fin.read().decode('utf-8'))  #utf-8 디코딩
    data = []
    for child in root:
        if len(child.find('stock_code').text.strip()) > 1: # 종목코드가 있는 경우
            data.append([]) #data에 append하라
            for item in items:
                data[-1].append(child.find(item).text)
    df = pd.DataFrame(data, columns=item_names)
    return df
stock_comp = get_corpcode("dad223eb446ae73419026f15c1593dcaab4bf35c")

bgn_de = '20200101'  # 시작일
end_de = '20220131'  # 종료일

for _, row in stock_comp.iterrows():
    corp_code = row['고유번호']
    stock_code = row['종목코드']

    url = f"https://opendart.fss.or.kr/api/cvbdIsDecsn.json?crtfc_key={crtfc_key}&corp_code={corp_code}&bgn_de={bgn_de}&end_de={end_de}"
    response = requests.get(url)
    data = json.loads(response.text)

    status = data.get('status')
    if status == '000':
        print(f"종목코드: {stock_code}")
        print("결산 정보:")
        print(data)
        print("---")
