from collections import deque

m, n = map(int, input().split())

matrix = []
queue = deque()

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
  matrix.append(list(map(int, input().split())))

def bfs():
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
        matrix[nx][ny] = matrix[x][y] + 1
        queue.append([nx, ny])

for i in range(n):
  for j in range(m):
    if matrix[i][j] == 1:
      queue.append([i, j])

bfs()

result = max(map(max, matrix)) - 1

for i in range(n):
  for j in range(m):
    if matrix[i][j] == 0:
      result = -1

print(result)

# 다른 풀이에 비해 장치가 많이 줄어든 코드가 과연 좋은 코드일까?? 