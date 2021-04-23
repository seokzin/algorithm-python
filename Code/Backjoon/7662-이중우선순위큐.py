import heapq
import sys

def sync(q):
  while q and id[q[0][1]] == 0:
    heapq.heappop(q)

for _ in range(int(input())): # t
  id = [0] * 1_000_000
  minH, maxH = [], []

  for i in range(int(input())): # k
    cmd, num = sys.stdin.readline().split()
    num = int(num)

    if cmd == 'I':
      heapq.heappush(minH, (num, i))
      heapq.heappush(maxH, (-num, i))
      id[i] = 1
    elif num == 1: 
      sync(maxH)
      if maxH:
        id[maxH[0][1]] = 0
        heapq.heappop(maxH)
    else:
      sync(minH)
      if minH:
        id[minH[0][1]] = 0
        heapq.heappop(minH)

  sync(maxH)
  sync(minH)

  if minH and maxH:
    print(-maxH[0][0], minH[0][0]) # heap[0] 은 최소값 출력
  else:
    print("EMPTY")

# 한쪽 힙 삭제시 다른쪽 동기화 해주는 것이 핵심. 이때 remove 같은 내장 함수보다 id를 통해 삭제하는 것이 빠른 연산 보장
# heapq에 대해 정리하자 - 힙푸쉬(힙, (우선순위, 값))
# 20라인 - num = '1'로 돼있어서 계속 틀렸음