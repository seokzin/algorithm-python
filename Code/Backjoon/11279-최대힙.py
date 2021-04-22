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
      print(-1 * heapq.heappop(hq))
  else:
    heapq.heappush(hq, -x)

# heapq가 min heap만 지원하기 때문에 음수 처리로 최대힙 구현