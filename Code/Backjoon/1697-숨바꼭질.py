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
      if (0 <= j < LIMIT) and visit[j] == 0:
        visit[j] = visit[i] + 1
        q.append(j)

n, k = map(int, input().split())
visit = [0] * LIMIT

bfs()

# 풀이마다 bfs의 인자가 0~3개 제각각이였다. 이를 비교해보면 좋을 듯