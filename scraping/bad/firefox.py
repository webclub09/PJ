from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
import datetime as dt

binary = FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
browser = webdriver.Firefox(executable_path='C:\python/geckodriver.exe',firefox_binary=binary)

startdate = dt.date(year = 2015, month=2, day=6)
untildate = dt.date(year = 2015, month=2, day=7)
enddate = dt.date(year = 2015, month=2, day=10)

totalfreq = []
## enddate 와 startdate 가 같아질때 까지 코드 반복
while not enddate == startdate:
## startdate 와 untilldate를 string으로 변환하여 URL 변수 설정
    url = 'https://twitter.com/search?q=사조 참치%20since%3A' + str(startdate) + '%20until%3A' + str(
        untildate) + '&amp;amp;amp;amp;amp;amp;lang=ko'
    browser.get(url)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    lastHeight = browser.execute_script("return document.body.scrollHeight")
    while True:
        dailyfreq = {'Date': startdate}
#     i=0 i는 페이지수
        wordfreq = 0
        tweets = soup.find_all("p", {"class": "TweetTextSize"})
        wordfreq += len(tweets)

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

        newHeight = browser.execute_script("return document.body.scrollHeight")
        print(newHeight)
        if newHeight != lastHeight:
            html = browser.page_source
            soup = BeautifulSoup(html, 'html.parser')
            tweets = soup.find_all("p", {"class": "TweetTextSize"})
            wordfreq = len(tweets)
        else:
            dailyfreq['Frequency'] = wordfreq
            wordfreq = 0
            totalfreq.append(dailyfreq)
# startdate는 untildate인 2월 6일로 untildate는 하루 더 늘어서 2월 7일이 됐다. 이런식으로 startdate가 enddate인 5월 7일까지 반복된다면 하루 하루 데이터를 뽑아낼 수 있다.
            startdate = untildate
            untildate += dt.timedelta(days=1)
            dailyfreq = {}
            break
#         i+=1
        lastHeight = newHeight
