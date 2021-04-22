import sys
# sys.setrecursionlimit(10 ** 4)

def dfs(n):
    visit[n] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)
            
N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visit = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)