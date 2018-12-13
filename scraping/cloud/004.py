import collections
import pytagcloud
import webbrowser

d_frequency = {
    '블랙 팬서':1339822000, #movieNm:salesAmt
    '골든슬럼버':363771900,
    '조선명탐정: 흡혈괴마의 비밀':296896400,
    '흥부: 글로 세상을 바꾼 자':126148600,
    '명탐정 코난:감벽의 관':78434800,
    '코코':56664400,
    '패딩턴 2':52331600,
    '리틀 포레스트':46692700,
    '그것만이 내 세상':45505700,
    '월요일이 사라졌다':17183800
}

d_frequency = collections.Counter(d_frequency)

tags = pytagcloud.make_tags(d_frequency.items(), maxsize=50) #모두
#tags = pytagcloud.make_tags(collections.Counter(d_frequency).most_common(50), maxsize=50) #상위 50개
pytagcloud.create_tag_image(tags, 'wc1.png', size=(900, 600), fontname='korean')
webbrowser.open('wc1.png')
