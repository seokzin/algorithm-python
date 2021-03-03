# 파이썬3은 자동 자료형 변환이 적용됨
print(5/2) # 2.5
print(4/2) # 2.0

# // : 버림 나눗셈 - 결과: .0으로 끝나는 실수. 나눗셈 몫 구할때 쓰임
print(5.5//2) # 2.0

# % : 나머지 연산
print(5%2) # 1

# ** : 거듭제곱
print(2**10) # 1024

# int(값): 값을 정수로 만들기
int(3.3) #3
int(5/2) #2
int('10') #10

# divmod: 몫과 나머지 함께 구하기
divmod(5, 2) # (2, 1)

# 진수
0b110 # 2진수 : 6
0o10 # 8진수 : 8
0xF # 16진수 : 15

# 실수 값의 오차
print(4.3 - 2.7) # 1.5999999999999996

# 실수와 정수 계산 - 표현 범위가 넓은 자료형으로 계산됨
print(4.2 + 5) # 9.2

# 값을 실수로 만들기
float(5) # 5.0
float(1+2) # 3.0
float('5.3') # 5.3