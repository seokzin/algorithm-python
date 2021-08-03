from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
degree = [0] * (n+1) # 진입차수 관리
res = []

q = deque()

for _ in range(m):
    order = list(map(int, input().split()))

    for i in range(1, order[0]):
        graph[order[i]].append(order[i+1])
        degree[order[i+1]] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)

while q:
    x = q.popleft()

    for y in graph[x]:
        degree[y] -= 1

        if degree[y] == 0:
            q.append(y)

    res.append(x)

if len(res) == n:  
    print(*res, sep='\n')
else:
    print(0)  # 순서를 정할 수 없다면

# 기본 위상정렬 문제