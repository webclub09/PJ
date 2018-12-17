##### 문자열
### 문자열 안에 작은 따옴표나 큰 따옴표를 포함시키고 싶을떄
# 1. 큰따옴표로 양쪽 둘러싸기
"Hello World"

# 2. 작은따옴표로 양쪽 둘러 싸기
'Python is Fun'

# 3. 큰따옴표 3개를 연속으로 써서 양쪽 둘러싸기
"""Life is too short, You need Python"""

# 4. 작은따옴표 3개를 연속으로 써서 양쪽 둘러싸기
'''Life is too short You need Python'''

## 문자열 안에 작은 따옴표나 큰 따옴표를 포함시키고 싶을 떄
# 1) 문자열에 작은 따옴표를 포함 시킬때
# 자열 중 Python's에 작은따옴표(')가 포함되어 있다.
# 다음과 같이 문자열을 큰따옴표(")로 둘러싸야 한다.
# 큰따옴표 안에 들어 있는 작은따옴표는 문자열을 나타내기 위한 기호로 인식되지 않는다.
food = "Python's favorite food is perl"
# 작은따옴표 안에 작은 따옴표가 있으면 오류 발생

# 2) 문자열에 큰따옴표 (")를 포함 시킬 떄
# 다음과 같이 문자열을 작은따옴표(')로 둘러싸면 된다.
say = '"Python is very easy." he says.'

# 3) \ 백슬래시를 이용하여 작은 따옴표와 큰 따옴표를 문자열에 포함시킬수 있다.
# 작은따옴표(')나 큰따옴표(")를 문자열에 포함시키는 또 다른 방법은 \(백슬래시)를 이용하는 것이다.
# 즉, 백슬래시(\)를 작은따옴표(')나 큰따옴표(") 앞에 삽입하면
# \(백슬래시) 뒤의 작은따옴표(')나 큰따옴표(")는 문자열을 둘러싸는 기호의 의미가 아니라
# 문자 ('), (") 그 자체를 뜻하게 된다.
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."


### 여러 줄인 문자열을 변수에 대입하고 싶을 때
# 1) 줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기
multiline = "Life is too short\nYou need python"

# 2) 연속된 작은따옴표 3개(''') 또는 큰따옴표 3개(""") 이용
# 작은 따옴표
multiline='''
Life is too short
You need python
'''

# or 큰 따옴표
multiline="""
Life is too short
You need python
"""
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

# 2) 문자열 곱하기

a = "Python"
print(a * 2)

# 3) 문자열 곱하기 응용

print("=" * 50)
print("My Program")
print("=" * 50)

### 문자열 인덱싱과 슬라이싱


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
