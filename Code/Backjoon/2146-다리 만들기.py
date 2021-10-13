from collections import deque

D = ((1, 0), (0, 1), (-1, 0), (0, -1))


def bfs(sx, sy, idx):  # 섬마다 인덱스 부여
    q = deque([(sx, sy)])
    visit[sy][sx] = 1
    arr[sy][sx] = idx

    while q:
        x, y = q.popleft()

        for dx, dy in D:
            nx, ny = x+dx, y+dy

            if 0 <= nx < n and 0 <= ny < n and arr[ny][nx] and not visit[ny][nx]:
                visit[ny][nx] = 1
                arr[ny][nx] = idx
                q.append([nx, ny])


def find(k):  # 가까운 섬 찾기
    while q:
        x, y = q.popleft()

        for dx, dy in D:
            nx, ny = x+dx, y+dy

            if 0 <= nx < n and 0 <= ny < n:
                if arr[ny][nx] != k and visit[ny][nx]:  # 다른 섬을 찾았을 때
                    return dist[y][x] - 1

                if not arr[ny][nx] and not dist[ny][nx]:  # 바다를 만났을 때
                    dist[ny][nx] = dist[y][x] + 1
                    q.append([nx, ny])


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * n for _ in range(n)]
res = float('inf')
idx = 1  # 섬 인덱스

for i in range(n):
    for j in range(n):
        if arr[j][i] == 1 and not visit[j][i]:
            bfs(i, j, idx)
            idx += 1

for k in range(1, idx):
    q = deque()
    dist = [[0] * n for _ in range(n)]

    for i in range(n):  # 해당 섬의 거리값을 모두 1로 초기화
        for j in range(n):
            if arr[j][i] == k:
                q.append([i, j])
                dist[j][i] = 1

    res = min(find(k), res)  # 해당 섬에서 가장 가까운 섬의 거리로 res 갱신

print(res)
