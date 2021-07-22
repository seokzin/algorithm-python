import sys
input = sys.stdin.readline

n = int(input())
cnt = [0] * 10001

for i in range(n):
  num = int(input())
  cnt[num] += 1

for i in range(10001):
  if cnt[i] != 0:
    for j in range(cnt[i]):
      print(i)

# print((str(i) + '\n') * cnt[i], end='')
# str의 곱셈을 출력 부분에 응용해봤었다. -> 이것때문에 메모리 초과가 떴다.. 왜지