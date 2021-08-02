from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    delay = [0] + list(map(int, input().split()))  # 건설 소요시간
    graph = [[] for _ in range(n+1)]
    degree = [0] * (n+1) # 진입차수 관리
    dp = [0] * (n+1)

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        degree[y] += 1

    q = deque()

    for i in range(1, n+1):
        if degree[i] == 0:
            q.append(i)
            dp[i] = delay[i]

    while q:
        a = q.popleft()
        
        for b in graph[a]:
            degree[b] -= 1

            dp[b] = max(dp[b], dp[a]+delay[b])

            if degree[b] == 0:
                q.append(b)

    win = int(input())  # 승리 위한 건물번호

    print(dp[win])

# 2252 위상정렬 기본 문제를 응용
# DP를 활용