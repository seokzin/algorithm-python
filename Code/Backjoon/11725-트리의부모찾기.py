import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(n):
  for i in graph[n]:
    if parent[i] == 0:
      parent[i] = n
      dfs(i)

n = int(input())

graph = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)] # visit 기능을 함께함

for _ in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

dfs(1)

for i in parent[2:]:
  print(i)