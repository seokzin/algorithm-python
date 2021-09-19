import copy
from collections import deque


def bfs(arr):
    global res

    D = ((1, 0), (0, 1), (-1, 0), (0, -1))

    q = deque()
    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                q.append([i, j])

    while q:
        x, y = q.popleft()

        for dx, dy in D:
            nx, ny = x+dx, y+dy

            if 0 <= nx < n and 0 <= ny < m:
                if not arr[nx][ny]:
                    arr[nx][ny] = 2
                    q.append([nx, ny])

    for row in arr:
        cnt += row.count(0)
        
    res = max(res, cnt)


def wall(x):
    if x == 3:
        arr_copy = copy.deepcopy(arr)
        bfs(arr_copy)
        return

    for i in range(n):
        for j in range(m):
            if not arr[i][j]:
                arr[i][j] = 1
                wall(x+1)
                arr[i][j] = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 0

wall(0)
print(res)

# N이 8까지니까 브루트 포싱이 가능하다.. N중 for문이라 터질 줄 알았음
# 더 수학적으로 개선 가능해 보이지만 어려워 보인다. 코테에선 이미 패스할 확률이 높다.