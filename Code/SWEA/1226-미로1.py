from collections import deque

def bfs():
    q = deque()
    
    for x in range(16): # 시작지점 탐색
        for y in range(16):
            if arr[y][x] == 2:
                q.append((x, y))
                arr[y][x] = 1

    while q:
        x, y = q.popleft()

        arr[y][x] = 1

        for d in D:
            nx, ny = x+d[0], y+d[1]

            if arr[ny][nx] == 0 or arr[ny][nx] == 3:
                q.append((nx, ny))

                if arr[ny][nx] == 3:
                    return 1

    return 0


for _ in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))
    
    print(f'#{tc}', bfs())

# 벽 덕분에 nx, ny의 범위 초과가 없습니다.