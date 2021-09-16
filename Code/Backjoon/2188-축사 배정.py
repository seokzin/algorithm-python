import sys
input = sys.stdin.readline


def dfs(x):
    if visit[x] == 1:
        return 0
    visit[x] = 1
    for i in arr[x]:
        if idx[i] == 0 or dfs(idx[i]):
            idx[i] = x
            return 1
    return 0


n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
idx = [0 for _ in range(m + 1)]
cnt = 0

for i in range(1, n+1):
    data = list(map(int, input().split()))

    for j in data[1:]:
        arr[i].append(j)

for i in range(1, n+1):
    visit = [0 for _ in range(n+1)]

    if dfs(i):
        cnt += 1

print(cnt)

# 왜 visit을 매번 선언하는걸까 + dfs 동작 방식이 이해가 미흡. 다시 이해하자
# 11375와 동일 문제