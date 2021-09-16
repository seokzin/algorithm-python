import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize


def dijkstra(n):
    heappush(heap, [0, n])
    dp[n][0] = 0

    while heap:
        w, x = heappop(heap)
        
        for nx, nw in graph[x]:
            wei = nw + w

            if wei < dp[nx][k-1]:
                dp[nx][k-1] = wei
                dp[nx].sort()
                heappush(heap, [wei, nx])


n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
dp = [[INF] * k for _ in range(n+1)]
heap = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

dijkstra(1)

for i in range(1, n+1):
    print(-1 if dp[i][k-1] == INF else dp[i][k-1])

# 다익스트라 개념이 흐릿하다. 다시 공부하자