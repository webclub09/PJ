#!/usr/bin/python
# -*- coding: cp949 -*-

import time
from datetime import date, timedelta
from twitterscraper import query_tweets
from twitterscraper.main import JSONEncoder
import json
import datetime as dt
from time import sleep

total = 0

today = date.today()
now = time.localtime()

with open('aa.txt', 'r', encoding='utf-8') as f:
    handles = f.readlines()

handles = [h.rstrip('�n') for h in handles]
ss = '_'
all_tweets = {}
if __name__ == '__main__':
    for handle in handles:

# ��¥ ���ź��� �������
#         all_tweets[handle] = query_tweets(f"from:{handle}", limit=1000, begindate=dt.date(2018,1,1), enddate=dt.date.today(), poolsize=10, lang='')

# between ����
         all_tweets[handle] = query_tweets(f"from:{handle}", begindate=dt.date(2010,11,1), enddate=dt.date(2018,11,7), poolsize=10, lang='ko')
         print ({handle})

# ��¥�� ���� Ŭ�θ�
#    with open('JSON/' + today.strftime('%Y-%m-%d ')+str(now.tm_hour)+str(ss)+str(now.tm_min)+str(ss)+str(now.tm_sec)+str(handles)+'.json', 'a', encoding='utf-8') as f:

# ���� �ϳ��� ��ġ��
    with open('JSON/'+ 'output01.json', 'w', encoding='utf-8') as f:
        json.dump(all_tweets, f, cls=JSONEncoder)
