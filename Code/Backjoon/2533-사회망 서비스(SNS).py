import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline 


def dfs(n):
    visit[n] = True
    dp[n][0] = 0
    dp[n][1] = 1

    for nx in graph[n]:
        if not visit[nx]:
            dfs(nx)
            dp[n][0] += dp[nx][1]  # 어답터 아닐 때 자식은 무조건 어답터
            dp[n][1] += min(dp[nx][0], dp[nx][1])  # 어답터일때, 자식의 어답터 유무를 고려


n = int(input())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
dp = [[0, 0] for _ in range(n+1)]  # 인덱스/얼리어답터 유무

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)

print(min(dp[1][0], dp[1][1]))

# 독립 집합