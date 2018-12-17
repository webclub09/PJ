##### 02-5 딕셔너리 자료형
### 딕셔너리란?
# 사람은 누구든지 "이름" = "홍길동", "생일" = "몇 월 며칠" 등으로 구분할 수 있다.
# 파이썬은 영리하게도 이러한 대응 관계를 나타낼 수 있는 자료형을 가지고 있다.
# 요즘 사용하는 대부분의 언어들도 이러한 대응 관계를 나타내는 자료형을 갖고 있는데,
# 이를 연관 배열(Associative array) 또는 해시(Hash)라고 한다.

# 파이썬에서는 이러한 자료형을 딕셔너리(Dictionary)라고 하는데,
# 단어 그대로 해석하면 사전이라는 뜻이다.
# 즉, people이라는 단어에 "사람", baseball이라는 단어에 "야구"라는 뜻이 부합되듯이
# 딕셔너리는 Key와 Value라는 것을 한 쌍으로 갖는 자료형이다.
# 예컨대 Key가 "baseball"이라면 Value는 "야구"가 될 것이다.

### 딕셔너리는 어떻게 만들까?
# 다음은 기본적인 딕셔너리의 모습이다.
# {Key1:Value1, Key2:Value2, Key3:Value3 ...}
# Key와 Value의 쌍 여러 개가 {과 }로 둘러싸여 있다.
# 각각의 요소는 Key : Value 형태로 이루어져 있고 쉼표(,) 로 구분되어 있다.
# ※ Key에는 변하지 않는 값을 사용하고,
# Value에는 변하는 값과 변하지 않는 값 모두 사용할 수 있다.

dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic)
#>> {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a = {1:'hi'}
print(a)
#>> {1: 'hi'}

a={'a':[1,2,3]}
print(a)
#>> {'a': [1, 2, 3]}

### 딕셔너리 쌍 추가, 삭제하기
# 1. 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b'
print(a)
#>> {1: 'a', 2: 'b'}

a['name'] = 'pey'
print(a)
#>> {1: 'a', 2: 'b', 'name': 'pey'}

a[3] = [1,2,3]
print(a)
#>> {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

## 2. 딕셔너리 요소 삭제하기
del a[1]
print(a)
#>> {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

### 딕셔너리를 사용하는 방법
grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
#>> 10
print(grade['julliet'])
#>> 99

a = {1:'a', 2:'b'}
print(a[1])
#>> a
print(a[2])
#>> b

### 딕셔너리 만들 때 주의할 사항
# 딕셔너리에서 KEY는 고유한 값이므로 중복되는 Key값을 설정해 놓으면 하나를 제외한
# 나머지 것들이 모두 무시된다는 점을 주의해야 한다.
# 다음 예에서 볼 수 있듯이 동일한 Key가 2개 존재할 경우 1:'a'라는 쌍이 무시된다.
# 이렇게 Key가 중복되었을 때 1개를 제외한 나머지 Key:Value 값이 모두 무시되는 이유는 Key를 통해서 Value를 얻는 딕셔너리의 특징에서 비롯된다.
# 즉, 동일한 Key가 존재하면 어떤 Key에 해당하는 Value를 불러야 할지 알 수 없기 때문이다.
a = {1:'a', 1:'b'}
print(a)
#>> {1: 'b'}

### 딕셔너리 관련 함수들
# Key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print (a.keys())
#>> dict_keys(['name', 'phone', 'birth'])

for k in a.keys():
    print(k)
#>> name
#>> phone
#>> birth

# dict_keys 객체를 리스트로 변환하려면 다음과 같이 하면 된다.
print(list(a.keys()))
#>> ['name', 'phone', 'birth']

# Value 리스트 만들기(values)
print(a.values())
#>> dict_values(['pey', '0119993323', '1118'])

# Key, Value 쌍 얻기(items)
print(a.items())
#>> dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

# Key: Value 쌍 모두 지우기(clear)
a.clear()
print(a)
#>> {}

# Key로 Value얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))
#>> pey
print(a.get('phone'))
#>> 0119993323

# 다만, 다음 예제에서 볼 수 있듯이 a['nokey']처럼
# a 딕셔너리에 없는 키로 값을 가져오려고 할 경우
# a['nokey']는 Key 오류를 발생시키고
# a.get('nokey')는 None을 리턴한다는 차이가 있다.
# 어떤것을 사용할지는 여러분의 선택이다.
print(a.get('nokey'))

# 딕셔너리 안에 찾으려는 key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신
# 가져오게 하고 싶을 때에는 get(x, '디폴트 값')을 사용하면 편리하다.
print(a.get('foo', 'bar'))

## 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a)
#>> True
print('email' in a)
#>> False

##### 연습문제
