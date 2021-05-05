import sys
sys.setrecursionlimit(10**9)

n = int(input())

graph = [[] for _ in range(n+1)] # 인덱스 맞추기 위해
parent = [0 for _ in range(n+1)] # 복사 수준이 어떻게 될까

for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(n):
  for i in graph[n]:
    if parent[i] == 0:
      parent[i] = n
      dfs(i)

dfs(1)

for i in parent[2:]:
  print(i)

# DFS는 재귀 리밋 풀어주기!
# 생각해보니 parent 리스트가 방문 체크 기능을 해주니 visit 리스트를 없앴다.
# 왜 자꾸 틀리다고 나오지? 심지어 구글 답안과 코드도 같던데?
# 해결 1. PyPy로 바꿔서 맞춘다.
# 해결 2. sys.readline을 도입 + 재귀 10억으로 늘리기. 다만 의문인건 안써도 맞춘 사람들은 뭘까.
# 백준 재귀에러 정리하기. 내가 10억을 해도 서버가 못버티면 무의미. 그래도 이번 문제를 통해 재귀 값은 클수록 좋다고 본다. 10**5는 틀렸고 10**9는 맞았다.