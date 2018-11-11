from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
import datetime as dt
import urllib.parse

binary=FirefoxBinary('C:/Program Files/Mozilla Firefox/firefox.exe')
browser=webdriver.Firefox(executable_path='C:/Python/geckodriver.exe',firefox_binary=binary)

# 검색을 위한 변수 설정
startdate=dt.date(year=2017,month=12,day=24)
untildate=dt.date(year=2017,month=12,day=25)
enddate=dt.date(year=2017,month=12,day=25)
keyword = urllib.parse.quote_plus("참치")

totalfreq=[]
tweet_bag=[]
while not enddate==startdate:
    url='https://twitter.com/search?q='+keyword+'%20since%3A'+str(startdate)+'%20until%3A'+str(untildate)+'&amp;amp;amp;amp;amp;amp;lang=ko'
    browser.get(url)
    html = browser.page_source
    soup=BeautifulSoup(html,'html.parser')

    lastHeight = browser.execute_script("return document.body.scrollHeight")

    while True:
        dailyfreq={'Date':startdate}
        wordfreq=0
        tweets=soup.find_all("p", {"class": "TweetTextSize"})
        wordfreq+=len(tweets)

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        newHeight = browser.execute_script("return document.body.scrollHeight")
        print(newHeight)
        if newHeight != lastHeight:
            html = browser.page_source
            soup=BeautifulSoup(html,'html.parser')
            tweets=soup.find_all("p", {"class": "TweetTextSize"})
            wordfreq=len(tweets)
            tweet_bag.append(tweets)
        else:
            dailyfreq['Frequency']=wordfreq
            wordfreq=0
            totalfreq.append(dailyfreq)
            startdate=untildate
            untildate+=dt.timedelta(days=1)
            dailyfreq={}
            break
        lastHeight = newHeight
        for tweet in tweet_bag:
            print(tweet)