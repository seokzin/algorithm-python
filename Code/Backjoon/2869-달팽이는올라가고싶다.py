a, b, v = map(int, input().split())

res = (v-a) / (a-b) + 1

print(int(res) if res == int(res) else int(res) + 1)

# 처음에 단순하게 while문 거칠때마다 하루씩 이동으로 했는데 TC 3에서 무한작동했다.
# 반복 작업은 일일히 하나씩 하지말고 묶어보려 노력하자.
# math 대신 삼항연산자를 통해 라이브러리 의존성 줄여보자. int(v)는 디폴트가 내림인가?