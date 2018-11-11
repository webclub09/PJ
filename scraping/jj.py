from twitterscraper import query_tweets
import datetime as dt
from time import sleep

if __name__ == '__main__':

    # 수집한 트윗을 저장할 파일이름/위치지정
    total = 0
    fname = 'json/json' + str(dt.date.today()) + '.txt'  # 저장이름.위치.날짜

    while True:
        size = 0
        file = open(fname, 'ab')
        for tweet in query_tweets('문재인 AND 대통령', limit=10, begindate=dt.date(2018, 6, 15), enddate=dt.date(2018, 7, 4)):
            file.write(str(tweet.timestamp).encode())
            file.write(tweet.text.encode('utf-8'))
            size = size + 1
            # 수집할 때마다 카운트 올림

            file.close()
            total = total + size
            print('수집한 트윗 총 개수', total)

            sleep(5)  # 트윗 수집 작업을 잠시 멈춤