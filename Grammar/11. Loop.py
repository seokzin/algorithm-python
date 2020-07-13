# for + range
for i in range(20):
    print('Hello, world!', i)

# reversed() - 숫자 순서 뒤집기
for i in reversed(range(10)):
    print('Hello, world!', i)

# 시퀀스 객체로 반복
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

for letter in 'Python':
    print(letter, end=' ') # P y t h o n


# While - 변화식 들어감!
i = 0                       # 초기식
while i < 100:              # while 조건식
    print('Hello, world!')  # 반복할 코드
    i += 1                  # 변화식

# tip: 난수 생성
import random

# random() - 0~1 사이 실수
random.random()

# randint(a, b) - a~b 사이 정수
random.randint(1, 6) # 1~6 사이 정수 (6 포함)

i = 0
while i != 3:    # 3이 아닐 때 계속 반복
    i = random.randint(1, 6)
    print(i)

# choice() - 시퀀스에서 무작위 추출
dice = [1, 2, 3, 4, 5, 6]
random.choice(dice)

# break: 제어흐름 중단
i = 0
while True:    # 무한 루프
    print(i)
    i += 1          # i를 1씩 증가시킴
    if i == 100:    # i가 100일 때
        break       # 반복문을 끝냄. while의 제어흐름을 벗어남

for i in range(10000):    # 0부터 9999까지 반복
    print(i)
    if i == 100:    # i가 100일 때
        break       # 반복문을 끝냄. for의 제어흐름을 벗어남

# continue: 제어흐름 유지, 코드 실행만 건너뜀
for i in range(100):
    if i % 2 == 0:
        continue # 아래 코드를 실행하지 않고 건너뜀
    print(i)

i = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue      # 아래 코드를 실행하지 않고 건너뜀
    print(i)

# 중첩 Loop
for i in range(5):          # 5번 반복. 바깥쪽 루프는 세로 방향
    for j in range(5):      # 5번 반복. 안쪽 루프는 가로 방향
        print('j:', j, sep='', end=' ')    # j값 출력. end에 ' '를 지정하여 줄바꿈 대신 한 칸 띄움
    print('i:', i, '\\n', sep='')    # i값 출력, 개행 문자 모양도 출력