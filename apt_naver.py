#tradeTypeCd (거래종류): all=전체, A1=매매, B1=전세, B2=월세, B3=단기임대

import requests
import json
import logging

URL = "https://m.land.naver.com/complex/getComplexArticleList"
text = (['3459','3294'])

param = {
    'hscpNo': text,  # 도원삼성래미안
#    'hscpNo': '3459',       # 도원삼성래미안
#    'hscpNo': '3294',       # 도화현대
#    'hscpNo': '407',        # 도화현대1차
#    'hscpNo': '23853',   # 세양청마루

    'tradTpCd': 'B1',       #tradeTypeCd (거래종류): all=전체, A1=매매, B1=전세, B2=월세, B3=단기임대
    'order': 'date_',
    'showR0': 'Y',
#    'tradCmplYn': 'N',
}

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.220 Whale/1.3.51.7 Safari/537.36',
    'Referer': 'https://m.land.naver.com/'
}

logging.basicConfig(level=logging.INFO)
page = 0

while True:
    page += 1
    param['page'] = page

    resp = requests.get(URL, params=param, headers=header)
    if resp.status_code != 200:
        logging.error('invalid status: %d' % resp.status_code)
        break

    data = json.loads(resp.text)
    result = data['result']
    if result is None:
        logging.error('no result')
        break

    for item in result['list']:
        if float(item['spc2']) < 50 or float(item['spc2']) > 100:
            continue
        logging.info('%s [%s] [%s] %s %s층 %s %s만원' % (item['cfmYmd'], item['atclNm'], item['tradTpNm'], item['bildNm'], item['flrInfo'], item['spc2'], item['prcInfo']))

    if result['moreDataYn'] == 'N':
        break
