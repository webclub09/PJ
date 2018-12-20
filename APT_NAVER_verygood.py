import re
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import pymysql
from datetime import datetime, timedelta
import time

nowtime = datetime.utcnow() + timedelta(hours=9)

# MySQL Connection 연결
conn = pymysql.connect(host='aa.co.kr', port=1, user='1', password='1!', db='python', charset='utf8')

curs = conn.cursor(pymysql.cursors.DictCursor)


# url = 'http://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=B1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1117012000' # 도원삼성레미안
# url = 'http://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=B1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1117012000' #
# url = 'http://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=B1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1117012000' #
# url = 'http://land.naver.com/article/articleList.nhn?rletTypeCd=A01&tradeTypeCd=B1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1117012000' #
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')

table = soup.find('table')
trs = table.tbody.find_all('tr')

# 거래, 종류, 확인일자, 매물명, 면적(㎡), 층, 매물가(만원), 연락처
for tr in trs[::2]:
    tds = tr.find_all('td')
    cols = [' '.join(td.text.strip().split()) for td in tds]

    if '_thumb_image' not in tds[3]['class']:  # 현장확인 날짜와 이미지가 없는 행
        cols.insert(3, '')

    거래 = cols[0]
    종류 = cols[1]
    확인일자 = datetime.strptime(cols[2], '%y.%m.%d.')
#    확인일자 = 확인일자.replace("00:00:00", "")
    현장확인 = cols[3]
    매물명 = cols[4]
    매물명 = 매물명.replace("네이버부동산에서 보기", "")
    매물명 = 매물명.replace("집주인 ", "")
    면적 = cols[5]
    공급면적 = re.findall('공급면적(.*?)㎡', 면적)[0].replace(',', '')
    전용면적 = re.findall('전용면적(.*?)㎡', 면적)[0].replace(',', '')
    공급면적 = float(공급면적)
    전용면적 = float(전용면적)
    층 = cols[6]
    매물가 = int(cols[7].replace(',', ''))
    연락처 = cols[8]
    입력날짜 = str(nowtime)

    if float(전용면적) < 50 or float(전용면적) > 80:
        continue

    print(거래, 종류, 확인일자, 현장확인, 매물명, 공급면적, 전용면적, 층, 매물가, str(nowtime))

##    # ==== insert example ====
    with conn.cursor() as curs:
        sql = """insert into tb_naverland(구분, 종류, 확인일자, 현장확인, 아파트명, 공급면적, 전용면적, 층, 매물가, 비고, 입력날짜) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"""
        curs.execute(sql, (거래, 종류, 확인일자, 현장확인, 매물명, 공급면적, 전용면적, 층, 매물가, '', 입력날짜))

    conn.commit()
