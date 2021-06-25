from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q.append([0, 0, 0])
  visit[0][0][0] = 1

  while q:
    x, y, z = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if a[nx][ny] == 0 and visit[nx][ny][z] == -1:
          visit[nx][ny][z] = visit[x][y][z] + 1
          q.append([nx, ny, z])
        # 아직 안뚫었는데 벽을 만났다면
        elif z == 0 and a[nx][ny] == 1 and visit[nx][ny][z+1] == -1:
          visit[nx][ny][z+1] = visit[x][y][z] + 1
          q.append([nx, ny, z+1])

n, m = map(int, input().split())
visit = [[[-1]*2 for _ in range(m)] for _ in range(n)]
q = deque()
a = []
res = visit[n-1][m-1]

for _ in range(n):
  a.append(list(map(int, input())))

bfs()

if res[0] == -1:
  print(res[1])
elif res[1] == -1:
  print(res[0])
else:
  print(min(res))

# 무식하게 벽 하나씩 부수며 카운팅할까? 너무 과부화같기도 하고
# 벽을 부숴서 손해보는 경우가 있을까? 있을법도 하다.
# BFS와 DP를 섞을 수 있나? 왜? 벽으로 인해 경우의 수가 생기기 때문인가?
# 2차원 배열문제는 BFS가 낫다고 한다. 왜?
# 벽을 안뚫을때 도착되는데 뚫어서 -1이 되는 경우가 있네.. 1 1 일때
# z=1 이 부순 위치를 기어갛는 것도 아닌데 어떤 원리로 최소값을 보장하는지는 잘 모르겠다. 예제를 손코딩 해야하는데 아직은 무리인듯..