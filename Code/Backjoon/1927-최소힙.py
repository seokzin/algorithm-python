import heapq
import sys

n = int(input())
hq = []

for _ in range(n):
  x = int(sys.stdin.readline())

  if x == 0:
    if not hq:
      print(0)
    else:
      print(heapq.heappop(hq))
  else:
    heapq.heappush(hq, x)

# 힙큐 라이브러리를 공부해보자
# 인풋 개수를 생각했으면 sys를 썼어야 한다. 또한 입력에 따른 시간 포스팅 정리하자. readline이 한번에 입력 받는 방식?