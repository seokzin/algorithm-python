n = int(input())
k = int(input())

graph = [[] for _ in range(n + 1)] # 인덱스 맞추기 위해
visit = [0] * (n + 1)

for _ in range(k):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(n):
  if visit[n] == 0:
    visit[n] = 1

    for j in graph[n]:
      dfs(j)

dfs(1)

print(sum(visit) - 1) # visit[1]은 뺀다.

# 그래프를 이중 리스트로 초기화하는 사례들은 무슨 이유?
# 함수에서 else를 생략하면 자동 return일까?