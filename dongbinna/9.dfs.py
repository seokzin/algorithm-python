# stack - append, pop
# queue - deque 라이브러리 - append, popleft
# queue를 기능적 구현 가능하나 시간 복잡도가 더 높아 라이브러리 추천

graph = [
  [], # 0번 시작 노드는 비워두기. 일반적으로 노드가 1부터 시작하기 때문
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

visited = [False] * 9 # [0]은 사용하지 않기 때문에 일부로 하나 더 큰 값으로 초기화

def dfs(graph, v, visited):
  visited[v] = True # 현재 노드를 방문 처리
  print(v, end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

dfs(graph, 1, visited)

# v = start node를 의미..?