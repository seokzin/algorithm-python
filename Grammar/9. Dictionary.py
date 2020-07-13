# 딕셔너리는 해시 형태로 값 저장
a = {'name': 'so', 'age': 26, 'tel': '010-1234-1234'}

# 중복키 불가
# b = {'age': 25, 'age': 26}

# 다양한 자료형
# but 키에는 List나 Dictionary 사용 불가
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}

# 빈 딕셔너리
x = {}
x = dict()

# dict 함수로 딕셔너리 만들기
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)

# zip 함수 활용
lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))

# (키, 값) 형식의 tuple 활용
lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])

# 딕셔너리 값 접근
lux1['health'] # 490

# 키가 있는지 확인
'health' in lux1 # T
'level' not in lux1 # F

# 키 개수
len(lux1)

# 딕셔너리 응용

# setdefault : 딕셔너리 키-값 쌍 추가
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e') # 'e' : None 추가
x.setdefault('f', 100) # 'f' : 100 추가

# update : 딕셔너리 값 수정
x.update(a=90)
x.update(a=900, f=60)

# pop, del : 키-값 쌍 삭제
x.pop('a')
del x['b']

# clear : 딕셔너리 비우기
x.clear()

# get : 딕셔너리 키의 값 불러오기
x.get('d') # 40

# items(), keys(), values() : 딕셔너리 특정 값들 불러오기
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.items() # 키-값 쌍 모두 불러오기 / dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])
x.keys() # 키 모두 가져오기 / dict_keys(['a', 'b', 'c', 'd'])
x.values() # 값 모두 가져오기 / dict_values([10, 20, 30, 40])

# fromkeys : 리스트, 튜플 -> 딕셔너리
keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys) # x = {'a': None, 'b': None, 'c': None, 'd': None}
y = dict.fromkeys(keys, 100) # y = {'a': 100, 'b': 100, 'c': 100, 'd': 100}

# 딕셔너리 값 출력
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

for i in x:
    print(i, end=' ') # a b c d

for key, value in x.items():
    print(key, value) # a 10 /n b 20 /n c 30 /n d 40



