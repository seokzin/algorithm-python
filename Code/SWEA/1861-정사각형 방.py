D = [(-1,0), (1, 0), (0, -1), (0, 1)]

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [0] * (n*n + 1)

    for x in range(n):
        for y in range(n):
            for dy, dx in D:
                nx, ny = x+dx, y+dy

                if 0 <= nx < n and 0 <= ny < n:
                    if arr[ny][nx] == arr[y][x]+1:
                        visit[arr[y][x]] = 1
                        break

    for i in range(n*n, 0, -1):  # 누적합 구하기 (역탐색)
        if visit[i-1] and visit[i]:
            visit[i-1] = visit[i]+1

    print(f'#{tc}', visit.index(max(visit)), max(visit)+1)