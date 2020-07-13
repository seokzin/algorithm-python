# Set : 집합 개념
fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}

# 요소는 중복 X
fruits = {'orange', 'orange', 'cherry'} # {'cherry', 'orange'}

# 특정 값 확인
'orange' in fruits # T

# set 만들기
a = set('apple') # {'e', 'l', 'a', 'p'}
b = set(range(5)) # {0, 1, 2, 3, 4}

# set 안에 set를 넣을 수 없다.
# a = {{1, 2}, {3, 4}} -> X

# 집합 연산
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# |, union : 합집합
a | b # {1, 2, 3, 4, 5, 6}
set.union(a, b) # {1, 2, 3, 4, 5, 6}

# &, intersection : 합집합
a | b # {3, 4}
set.intersection(a, b) # {3, 4}

# -, difference : 차집합
a - b # {1, 2}
set.difference(a, b) # {1, 2}

# ^, symmetric_difference : XOR (겹치지 않는 요소만 포함)
a ^ b # {1, 2, 5, 6}
set.symmetric_difference(a, b) # {1, 2, 5, 6}

# add : 세트에 요소 추가
a = {1, 2, 3, 4}
a.add(5) # a = {1, 2, 3, 4, 5}

# remove : 특정 요소 삭제 + 요소 없으면 에러
a.remove(3) # a = {1, 2, 4, 5}

# discard : 특정 요소 삭제 + 요소 없으면 넘어감
a.discard(3)

# pop : 임의의 요소 삭제
a.pop()

# clear : 모든 요소 삭제
a.clear()

# 요소 개수 구하기
len(a)

# 세트의 할당과 복사
a = {1, 2, 3, 4}

b = a # 같은 세트를 가리킴
b = a.copy() # 독립적인 세트가 됨