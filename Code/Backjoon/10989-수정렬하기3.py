import sys

cnt = [0] * 10001 # 메모리 제약상 중복수를 카운트한다.

n = int(sys.stdin.readline())

for _ in range(n):
  num = int(sys.stdin.readline())
  cnt[num] += 1

for i in range(10001):
  if cnt[i] > 0:
    print((str(i) + '\n') * cnt[i], end='')

# 2750 문제에 비해 input이 대거 늘었다.
# 1. readline() 으로 변경해준다.
# 2. 배열의 구조를 바꿔준다. 근데 배열이 왜 메모리 초과가 뜨지?

# 출력을 for문 말고 다른 방법을 써보고 싶어서 괴상하게 짜버렸다. str은 곱셈이 된다는 점에 착안. 엄격히는 숫자가 아닌 문자를 출력한거니까..