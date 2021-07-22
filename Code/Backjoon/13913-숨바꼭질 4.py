from collections import deque

LIMIT = 100001

def bfs():
  q = deque()
  q.append(n)

  while q:
    x = q.popleft()

    if x == k:
      print(visit[x])
      ans = [x]

      while x != n:
        x = path[x]
        ans.append(x)

      print(*ans[::-1])
      return

    for nx in (x-1, x+1, x*2):
      if 0 <= nx < LIMIT and visit[nx] == 0:
        visit[nx] = visit[x]+1
        path[nx] = x
        q.append(nx)

n, k = map(int, input().split())
visit = [0] * LIMIT
path = [0] * LIMIT # path[현재] = 이전좌표

bfs()

# visit[n] = 1 하면 n=k일 때 틀린다. if에서 알아서 필터링 된다.