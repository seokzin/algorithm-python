# type(값): 객체(변수)의 자료형 알아내기
type(10) # <class 'int'>
type(3.5) # <class 'float'>
type(y) # <class 'string'>

# 변수 여러개 만들기
x, y, z = 10, 20, 30
a = b = c = 10

# 입력 값을 변수 두 개에 저장하기
# split() : 문자 기준으로 분리
a, b = input().split()

# map() : 원하는 자료형으로 변환하기
map(int, '53')
map(int, input().split())