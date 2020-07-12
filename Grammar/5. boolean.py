10 == 10 # T
10 != 5 # T

'Python' == 'Python' # T
'Python' == 'python' # F

# is, is not : '객체'가 같은지 비교. 주소 비교 방식이라 값 비교에는 쓰지 않기.
1 == 1.0 # T
1 is 1.0 # F
1 is not 1.0 # T

# 논리 연산자
True and False # F
True or False # T
not True # F

# 비교 연산자 + 논리 연산자
10 == 10 and 10 > 5 # T

# 정수, 실수의 boolean 값
# 정수 0, 실수 0.0이외의 모든 숫자는 True입니다. 그리고 빈 문자열 '', ""를 제외한 모든 문자열은 True입니다.
bool(1) # T
bool(0) # F
bool(1.5) # T
bool(0.0) # F
bool('false') # T
bool('') # F

