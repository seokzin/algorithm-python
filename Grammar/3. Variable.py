# 변수 만들기
x = 10
y = 'hello world'

# type(값): 객체(변수)의 자료형 알아내기
type(10) # <class 'int'>
type(3.5) # <class 'float'>
type(y) # <class 'string'>

# 변수 여러개 만들기
x, y, z = 10, 20, 30
a = b = c = 10

# 변수 삭제하기
x = 10
del x

# 빈 변수 만들기 (= Null)
x = None

# 변수 계산하기
a = 10
a += 20 # a = 30

# 변수 부호 붙이기
x = -10
+x # -10
-x # 10

# input(): 입력 값을 변수에 저장하기
x = input()
print(x)

y = input('숫자를 입력하세요: ')
print(y)

# 입력 값을 변수 두 개에 저장하기
# split() : 문자 기준으로 분리
a, b = input('문자열 두 개를 입력하세요: ').split()
print(a)
print(b)

# map() : 원하는 자료형으로 변환하기
map(int, '53')
map(int, input('두 숫자를 입력하세요: ').split())

# split(문자) : 문자 기준으로 분리
input('숫자 두 개를 입력하세요: ').split(',')