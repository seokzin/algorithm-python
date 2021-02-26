# 미로 탈출 - bfs (최단거리와 관련). 모든 노드의 최단거리 값을 비교해보자.

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue: # 큐가 빌때까지 반복
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 0: 
        continue # 벽인 경우 무시
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny)) # 해당 노드를 처음 방문하면 최단 거리 기록
        
  return graph[n-1][m-1] # 우하단까지 최단 거리 반환



print(bfs(0, 0))
  
# 9 - input()도 문자열=리스트 임을 인지하자..