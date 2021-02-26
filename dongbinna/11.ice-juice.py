# 2차원 리스트 내에서 연결 요소들 찾아 아이스크림으로 묶기
# 2차원 리스트도 경로를 연결해 그래프로 나타낼 수 있다 - dfs/bfs 사용 가능해진다.

# 방문하지 않은 지점을 카운트 하면 된다..?

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

def dfs(x, y):
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False # 범위 벗어나면 즉시 종료
    
  if graph[x][y] == 0: # 방문하지 않았다면
    graph[x][y] = 1 # 방문 처리
    # 상하좌우 재귀 호출
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False

result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      result += 1

print(result)

# 어렵다..
# 8 - 인풋으로 2차원 리스트 만드는 법
# 23, 24 리턴값의 의미란..? 왜 T랑 F로 방문 여부를 따지지 이부분은 이해 못하고 넘어가게 되었다.