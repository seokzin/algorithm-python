from collections import deque

n, m = map(int, input().split())

dx = [0,1,0,-1]
dy = [-1,0,1,0]
graph = [list(input()) for _ in range(n)]
cost = [[0]*n for _ in range(n)] # 걸음수
node = [] # 노드, 비용 저장 -> 크루스칼 알고리즘 위해

def bfs(x, y):
  queue = deque()
  queue.append((x,y))

  while queue:
    x,y = queue.popleft()

    for i in range(4):
      nx,ny = x+dx[i], y+dy[i]

      if nx<0 or ny<0 or nx>=n or ny>=n:
        continue
      if graph[nx][ny] == '1':
        continue
      if (graph[nx][ny] == '0' or graph[nx][ny] == 'K' or graph[nx][ny] == '0') and cost[nx][ny] == 0:
        cost[nx][ny] = cost[x][y] + 1

        queue.append((nx,ny))

  return cost

# S 위치 찾기
for i in range(n):
  for j in range(n):
    if graph[i][j] == 'S':
      bfs(j, i)

############ 크루스칼 알고리즘

# k1과 k2 사이 거리는 어떻게 구하지?
# 어려워서 멈췄습니다. 나중에 다시 매꾸겟습니다..