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

# 리스트 응용
# append : 끝에 요소 추가
a = [1, 2, 3]
a.append(4) # a = [1, 2, 3, 4]
a.append([5, 6]) # a = [1, 2, 3, 4, 5, 6]

# extend : 리스트 끝에 다른 리스트 연결
a.extend([7, 8]) # a = [1, 2, 3, 4, 5, 6, 7, 8]

# insert : 특정 위치(인덱스)에 추가
a.insert(2, 500) # a = [1, 2, 500, 3...]

# pop : 마지막 요소 삭제 후 반환 / del a[] : 삭제만
a.pop() # 8

# remove : 리스트의 특정 값 삭제
a.remove(500)

# index(값) : 특정 값의 인덱스 출력
a.index(3) # 2

# count(값) : 특정 값의 개수 구하기
a = [1, 1, 1, 2, 3]
a.count(1) # 3

# reverse : 리스트 순서 뒤집기
a.reverse()

# sort : 리스트 요소 정렬(오름차순) + 리스트 변경
# sorted : 리스트 요소 정렬 + 정렬된 새 리스트 생성
a.sort()
sorted(a) # 정렬된 새 리스트 생성

# clear : 리스트 모든 요소 삭제
a.clear() # a = []

# 리스트 할당 및 복사
a = [0, 0, 0, 0, 0]
b = a # 실제로는 리스트 한 개. a와 b가 같은 리스트를 가리킴
a is b # T

c = a.copy # 값이 같은 별개의 리스트 c를 만듦
a is c # F

# 리스트 요소 출력
a = [38, 21, 53, 62, 19]
for i in a:
    print(i) # 줄 바꾸며 모든 값 출력

i = 0
while i < len(a):
    print(a[i])
    i += 1

# enumerate(리스트, start) : 원하는 인덱스부터 출력
for index, value in enumerate(a, start=1):
    print(index, value)

# min, max : 리스트의 최소, 최대값 출력
min(a) # 19
max(a) # 62

# sum : 리스트 값 합계 출력
sum(a)

# 리스트 표현식
a = [i for i in range(10)] # a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = list(i for i in range(10)) # b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

a = [i for i in range(10) if i % 2 == 0] # a = [0, 2, 4, 6, 8]


# map : map은 리스트 및 모든 반복 가능한 객체의 요소들에 대해 지정된 함수로 한번에 처리해주는 함수(map은 원본 리스트를 변경하지 않고 새 리스트를 생성)
a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a)) # a = {1, 2, 3, 4]

# map 함수 사용시 map 객체 반환
x = input().split()    # input().split()의 결과는 문자열 리스트
m = map(int, x)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
a, b = m               # 맵 객체는 변수 여러 개에 저장할 수 있음

# 튜플 응용 - 리스트 응용과 비슷하나 값 변경, 삭제 불가. 암기 XX
a = (10, 20, 30, 15, 20, 40)

# index
a.index(10) # 0

# count
a.count(20) # 2

# 튜플 요소 출력
for i in a:
    print(i, end=' ')

# 튜플 표현식식
a = tuple(i for i in range(10) if i % 2 == 0) # a = (0, 2, 4, 6, 8)

# 튜플에 map 사용
a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a)) # a = (1, 2, 3, 4)

# min, max, sum
min(a) # 1
max(a) # 4
sum(a) # 10


# 2차원 리스트
a = [[10, 20], [30, 40], [50, 60]]

a = [[10, 20],
     [30, 40],
     [50, 60] ]

a[0][0] # 10
a[2][1] # 60

# 반복문으로 2차원 리스트 만들기
a = []  # 빈 리스트 생성
for i in range(3):
    line = []  # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        line.append(0)  # 안쪽 리스트에 0 추가
    a.append(line)  # 전체 리스트에 안쪽 리스트를 추가

# 리스트 표현식으로 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)] # a = [[0, 0], [0, 0], [0, 0]]

# 2차원 튜플 - 리스트와 동일
a = ((10, 20), (30, 40), (50, 60)) # a = [[0, 0], [0, 0], [0, 0]]

# 2차원 리스트 복사
import copy

b = a.copy() # 같은 리스트를 가리킴
b = copy.deepcopy(a) # 독립적인 리스트 b 생성