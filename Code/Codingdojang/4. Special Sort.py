# n개의 정수를 가진 배열이 있다. 이 배열은 양의정수와 음의 정수를 모두 가지고 있다. 이제 당신은 이 배열을 좀 특별한 방법으로 정렬해야 한다.
# 정렬이 되고 난 후, 음의 정수는 앞쪽에 양의정수는 뒷쪽에 있어야 한다. 또한 양의정수와 음의정수의 순서에는 변함이 없어야 한다.
# 예. -1 1 3 -2 2 ans: -1 -2 1 3 2.

# 내 아이디어: List에 insert를 통해 특정 위치에 삽입.
# 음수는 왼쪽에서 밀어낸다. - insert(0, num)
# 양수는 오른쪽에서 밀어낸다. - append(num) 또는 insert(len(a)-1, num)

# 강의 아이디어: python queue를 사용. 2개의 큐에 음수, 양수 분리하고 이후 합쳐서 호출
# 생각해보니 2개의 시퀀스로 나누면 삽입 위치를 고려할 필요가 없어진다.
# but 실전에선 queue 풀이는 너무어렵다. List로도 충분하나 공부용으로는 시도할 만하다.

# tip 1. 파이썬의 자료구조 라이브러리를 잘 익히자. 구글링을 통해 찾아보자.
# tip 2. 특수값(0, 경계값)일 때 결과 해보기. 여기선 양, 음의 정수 명시해서 0 취급 X
# tip 3. 막히면 debugging 기능을 활용하자. 변수에 담긴 값 등을 볼 수 있다.
# tip 4. 변수가 여러번 사용될 수 있으니 넘버링을 고려하자. ex) list1, list2

import queue

q1 = queue.Queue()
q2 = queue.Queue()

# queue는 초기 선언 불가(?). put을 통해 값을 집어 넣어야 함
for i in [-1, 1, 3, -2, 2]:
    if i < 0:
        q1.put(i)
    elif i > 0:
        q2.put(i)

print(list(q1.queue + q2.queue))

# list 풀이
list1 = [-1, 1, 3, -2, 2]
print([i for i in list1 if i < 0] + [i for i in list1 if i > 0])