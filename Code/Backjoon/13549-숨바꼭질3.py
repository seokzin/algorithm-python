from collections import deque

LIMIT = 100001

def bfs():
  q = deque()
  q.append(n)

  while q:
    i = q.popleft()

    if i == k:
      print(visit[i])
      return

    for j in (i - 1, i + 1, i * 2):
      if 0 <= j < LIMIT and not visit[j]:
        if j == i * 2 and i != 0:
          visit[j] = visit[i] 
          q.appendleft(j)
        else:
          visit[j] = visit[i] + 1
          q.append(j)

n, k = map(int, input().split())
visit = [0] * LIMIT

bfs()

# for .. in 문법 꽤나 유익하다. 다시금 정리해보자.
# i != 0 인 이유 -> j = (-1, 1, 0)이 됨. -1은 L17, 1은 L21에서 동작. 0은 무한루프 발생