# List
a = [1, 2, 3, 4, 5]
b = ['hello', 17, 13.3, True]
c = [] # 빈 리스트
d = list() # 빈 리스트

# range()
range(10) # 0 포함 X
range(0,10) # 0 포함 X

# range를 이용한 리스트 생성
a = list(range(10)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = list(range(5, 12)) # [5, 6, 7, 8, 9, 10, 11]
c = list(range(-4, 10, 2)) # [-4, -2, 0, 2, 4, 6, 8] / 증가폭 = 2


# Tuple
# 리스트와 달리 요소 변경, 추가, 삭제 불가 (읽기 전용 리스트)
a = (1, 2, 3, 4, 5)
b = ('hello', 17, 13.3, True)

# 값 한개일때
(38) # 38 / int
(38, ) # (38,) / tuple

# Tuple <-> List
a = [1, 2, 3]
tuple(a)

b = (1, 2, 3)
list(b)

# List, Tuple의 변수화
a, b, c = [1, 2, 3]
print(a, b, c) # 1 2 3

d, e, f = (4, 5, 6)
print(d, e, f) # 4 5 6

# Packing : 변수에 리스트 또는 튜플을 할당하는 과정
a = [1, 2, 3]    # 리스트 패킹
b = (1, 2, 3)    # 튜플 패킹
c = 1, 2, 3      # 튜플 패킹
