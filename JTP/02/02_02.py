##### 02_02 문자열
### 문자열 안에 작은 따옴표나 큰 따옴표를 포함시키고 싶을떄
# 1. 큰따옴표로 양쪽 둘러싸기
print("Hello World")
#>> Hello World

# 2. 작은따옴표로 양쪽 둘러 싸기
print('Python is Fun')
#>> Python is Fun

# 3. 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
print("""Life is too short, You need Python""")
#>> Life is too short, You need Python

# 4. 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
print('''Life is too short, You need Python''')
#>> Life is too short, You need Python

## 문자열 안에 작은 따옴표나 큰 따옴표를 포함시키고 싶을 떄
# 1) 문자열에 작은 따옴표를 포함 시킬때
# 자열 중 Python's에 작은따옴표(')가 포함되어 있다.
# 다음과 같이 문자열을 큰따옴표(")로 둘러싸야 한다.
# 큰따옴표 안에 들어 있는 작은따옴표는 문자열을 나타내기 위한 기호로 인식되지 않는다.
food = "Python's favorite food is perl"
print(food)
#>> Python's favorite food is perl

# 작은따옴표 안에 작은 따옴표가 있으면 오류 발생

# 2) 문자열에 큰따옴표 (")를 포함 시킬 떄
# 다음과 같이 문자열을 작은따옴표(')로 둘러싸면 된다.
say = '"Python is very easy." he says.'
print(say)
#>> "Python is very easy." he says.

# 3) \ 백슬래시를 이용하여 작은 따옴표와 큰 따옴표를 문자열에 포함시킬수 있다.
# 작은따옴표(')나 큰따옴표(")를 문자열에 포함시키는 또 다른 방법은 \(백슬래시)를 이용하는 것이다.
# 즉, 백슬래시(\)를 작은따옴표(')나 큰따옴표(") 앞에 삽입하면
# \(백슬래시) 뒤의 작은따옴표(')나 큰따옴표(")는 문자열을 둘러싸는 기호의 의미가 아니라
# 문자 ('), (") 그 자체를 뜻하게 된다.
fooda = 'Python\'s favorite food is perl'
print(fooda)
#>> Python's favorite food is perl

saya = "\"Python is very easy.\" he says."
print(saya)
#>> "Python is very easy." he says.



### 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 1) 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\nYou need python"
print(multiline)
#>> Life is too short
#>> You need python


# 2) 연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 이용
# 작은 따옴표
multiline='''
Life is too short
You need python
'''
print(multiline)
#>> Life is too short
#>> You need python


# or 큰 따옴표
multiline="""
Life is too short
You need python
"""
print(multiline)
#>> Life is too short
#>> You need python

## 이스케이프 코드란?
# 이스케이프 코드란 프로그래밍할 때 사용할 수 있도록 미리 정의해 둔 "문자 조합"이다.
# 주로 출력물을 보기 좋게 정렬하는 용도로 이용된다.
# 몇 가지 이스케이프 코드를 정리하면 다음과 같다.
### 코드 / 설명
# \n / 개행(줄바꿈)
# \t / 수평 탬
# \\ / 문자"\"
# \' / 단일 인용부호(')
# \" / 이중 인용부호(")
# \r / 캐리지 리컨
# \f / 폼피드
# \a / 벨 소리
# \b / 백 스페이스
# \000 / 널문자

### 문자열 연산하기
# 1) 문자열 더해서 연결하기
head = "Python"
tall = " is fun"
print(head + tall)
#>> Python is fun

# 2) 문자열 곱하기
a = "Python"
print(a * 2)
#>> PythonPython

# 3) 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)
#>> ==================================================
#>> My Program
#>> ==================================================

### 문자열 인덱싱과 슬라이싱
a = "Life is too short, You need Python"
print(a[3]) # e
#>> e

print(a[12]) # s
#>> s

print(a[-1]) # n -는 뒤에서 부터
#>> n

print(a[-0]) # L -0 은 0 과 같음
#>> L

print(a[0] + a[1] + a[2] + a[3]) # 0+1+2+3
#>> Life

print(a[0:4]) # 0부터 4까지 하지만 끝번호는 포함되지 않는다. 0 <= a < 4
#>> Life

print(a[0:3]) # 0부터 3까지 하지만 끝번호는 포함되지 않는다. 0 <= a < 3
#>> Lif

print(a[0:5]) # 0부터 5까지 하지만 끝번호는 포함되지 않는다. 0 <= a < 5
#>> Life

print(a[5:7]) # 5부터 7까지 하지만 끝번호는 포함되지 않는다. 5 <= a < 7
#>> is

print(a[12:17]) # 12부터 17까지 하지만 끝번호는 포함되지 않는다. 12 <= a < 17
#>> short

print(a[19:]) # 19번 부터 끝까지
#>> You need Python

print(a[:17]) # 처음부터 17번 까지
#>> Life is too short

print(a[:]) # 처음부터 끝까지
#>> Life is too short, You need Python

print(a[19:-7]) # 19번부터 -8까지 -7은 역시 포함되지 않음
#>> You need

### 슬라이싱으로 문자열 나누기
b = "20010331Rainy"
date = b[:8]
day = b[4:8]
weather = b[8:]
print (date)
#>> 20010331

print (day)
#>> 0331

print(weather)
#>> Rainy


### 문자열 바꾸기
c = "Pithon"

print(c[0]+'y'+c[2:])
#>> Python

### 문자열 포매팅

# 숫자 바로 대입
"I eat %d apples." %3

# 문자 바로 대입
"I eat %s apples." %"five"

# 숫자 ㄱ밧을 나타내는 변수로 대입
number = 3
"I eat %d apples." %number

#2개 이상의 값 넣기
number = 3
day = "three"
"I eat %d apples. %s days " %(number, day)


#### 문자열 포멧코드
# %s  문자열(string)
# %c  문자 1개(charactor)
# %d  정수
# %f  부동 소수
# %o  8진수
# %x  16진수
# %%  Literal % (문자 '%' 자체)

#포매팅 연산다 %d와 퍼센트를 같이 쓸때는 %%을 쓴다.
d = "현재 습도는 %d%%" %60
print(d)
#>> 현재 습도는 60%

###포맷 코드와 숫자 함께 사용하기
# 1) 정렬과 공백
# "%10s"는 전체 길이가 10인 문자열 공간에서
# hi를 오른쪽으로 정렬하고 그 앞이 나머지는 공백으로 남겨 두라는 의미
e = "%10s" % "hi"
print(e)

# 반대로 왼쪽 정렬은
f = "%-10sjane." % 'hi'
print(f)

# 2) 소수점 표현하기 소수점 4자리까지 표현
g = "%0.4f" % 3.42134234
print(g)

# 전체길이가 10개인 문자열 공간에서 오른쪽으로 정렬하는 예
h = "%10.4f" % 3.42134234
print(h)

### format 함수를 이용한 포매팅
# 숫자 바로 대입하기
i = "I eat {0} apples.".format(3)
print(i)

# 문자 바로 대입하기
j = "I eat {0} apples.".format('five')
print(j)

# 숫자 값을 가진 변수로 대입하기
number = 3
k = "I eat {0} apples.".format(number)
print(k)

# 2개 이상의 값 넣기
number = 10
day = "three"
l = "I ate {0} apples. so I was sick for {1} days.".format(number, day)
print(l)

# 이름으로 넣기
m = "I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
print(m)

# 인덱스와 이름을 혼용해서 넣기
n = "I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
print(n)

# 왼쪽 정렬
# :< 왼쪽정렬
print("{0:<10}".format("hi"))

# 오른쪽 정렬
# :> 오른쪽정렬
print("{0:>10}".format("hi"))

# 가운데 정렬
# :^ 기호를 이용하면 가운데 정렬
print("{0:^10}".format("hi"))

# 공백 채우기
# ^ 으로 가운데 정렬하고 = 으로 빈 공간 채움
print("{0:=^10}".format("hi"))
# < 으로 왼쪽 정렬하고 ! 으로 빈 공간 채움
print("{0:!<10}".format("hi"))

# 소수점 표현하기
o = 3.42134234
print("{0:0.4f}".format(o))

p = 3.42134234
print("{0:10.4f}".format(p))

# { 또는 } 문자 표현하기
q = "{{ and }}".format()
print(q)

### f 문자열 포매팅
# f 접두사를 붙이면 f 문자열 포매팅 기능을 사용할 수 있다.
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살 입니다.')

# 딕셔너리는 f 문자열에서 다음과 같이 사용가능하다.
d = {'name':'홍길동', 'age':30}
print (f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

# 정렬
print(f'{"hi":<10}')  # 왼쪽 정렬
print(f'{"hi":>10}')  # 오른쪽 정렬
print(f'{"hi":^10}')  # 가운데 정렬

# 공백 채우기
print(f'{"hi":=^10}')  # 가운데 정렬하고 '=' 문자로 공백 채우기
print(f'{"hi":!<10}')  # 왼쪽 정렬하고 '!' 문자로 공백 채우기

# 소수점
y = 3.42134234
print(f'{y:0.4f}')  # 소수점 4자리까지만 표현
print(f'{y:10.4f}')  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤

# f 문자열에서 '{' 나 '}' 문자를 사용하려면 다음과 같이 해야 한다.
print(f'{{ and }}')


### 문자열 관련 함수들
# 문자 개수 세기(count)
a = "hobby"
print(a.count('b'))

# 위치 알려주기1(find)
# 문자열 중 문자 b가 처음으로 나온 위치를 반환한다.
# 만약 찾는 문자나 문자열이 존재하지 않는다면 -1을 반환한다.
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k'))

# 위치 알려주기2(index)
# 문자열 중 문자 t가 맨 처음으로 나온 위치를 반환한다.
# 만약 찾는 문자나 문자열이 존재하지 않는다면 오류를 발생시킨다.
# 앞의 find 함수와 다른 점은 문자열 안에 존재하지 않는 문자를 찾으면 오류가 발생한다는 점이다.
a = "Life is too short"
print(a.index('t'))
#print(a.index('k'))

# 문자열 삽입(join)
a = ","
print(a.join('abcd'))

# abcd라는 문자열의 각각의 문자 사이에 변수 a의 값인 ','를 삽입한다.
# 보통 삽입할 문자를 변수로 지정하지 않고 다음처럼 많이들 사용한다.
print(",".join('abcd'))
# join 함수의 입력으로 리스트를 사용하는 예는 다음과 같다.
print(",".join(['a','b','c','d']))

#소문자를 대문자로 바꾸기(upper)
a = "hi"
print(a.upper())

# 대문자를 소문자로 바꾸기(lower)
a = "HI"
print(a.lower())

# 왼쪽 공백 지우기(lstrip)
a = " hi "
print(a.lstrip())

# 오른쪽 공백 지우기(rstrip)
a = " hi "
print(a.rstrip())

# 양쪽 공백 지우기(strip)
a = " hi "
print(a.strip())

# 문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기(split)
a = "Life is too short"
print(a.split())
a = "a:b:c:d"
print(a.split(':'))

##### 연습문제

## 문제 1
# 문자열 출력1
print('"점프 투 파이썬" 문제를 풀어보자')

## 문제 2
# 문자열 출력2
print("Life is too short \nYou need Python")

## 문제 3
# 공백 추가
print(' ' * 24 + "PYTHON")
print("%30s" % "PYTHON")

## 문제 4
# 문자열나누기
pin = "881120-1068234"
print (pin[:6])
print (pin[7:])

## 문제 5
# 문자열나누기
pin = "881120-1068234"
print (pin[7])

## 문제 6
# 문자열 변경
a = "1980M1120"
aa = a[:4]
bb = a[4]
cc = a[5:]
print(bb + aa + cc)

## 문제 7
# 문자열 찾기
a = "Life is too short, you need python"
print(a.index("short"))

## 문제 8
# 문자열 바꾸기1
a = "a:b:c:d"
print(a.replace(":","#"))

## 문제 9
# 문자열 바꾸기2
a = "a:b:c:d"
b = a.split(":")
print(b)
c = "#".join(b)
print(c)

