from collections import deque


def move(x, y, dx, dy):
    cnt = 0

    while arr[x+dx][y+dy] != '#' and arr[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1

    return x, y, cnt


def solve():
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))

    while q:
        rx, ry, bx, by, step = q.popleft()

        if step > 10:
            break

        for d in D:  # 4방향 이동 시도
            nrx, nry, rcnt = move(rx, ry, d[0], d[1])
            nbx, nby, bcnt = move(bx, by, d[0], d[1])

            if arr[nbx][nby] != 'O':  # B가 구멍에 안 갔을때만
                if arr[nrx][nry] == 'O':
                    return step

                if (nrx, nry) == (nbx, nby):
                    if rcnt > bcnt:  # 이동거리가 많은 것을 뒤로
                        nrx -= d[0]
                        nry -= d[1]
                    else:
                        nbx -= d[0]
                        nby -= d[1]

                if not visit[nrx][nry][nbx][nby]:
                    visit[nrx][nry][nbx][nby] = 1
                    q.append((nrx, nry, nbx, nby, step+1))
        
    return -1


n, m = map(int, input().split())
arr = [input() for _ in range(n)]
visit = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]  # 4차원 rx,ry,bx,by
q = deque()
rx, ry, bx, by = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        elif arr[i][j] == 'B':
            bx, by = i, j
q.append((rx, ry, bx, by, 1))
visit[rx][ry][bx][by] = 1

print(solve())

# 아.. 구현 방식은 이해가 가는데 소화는 안됐다. 나중에 다시 보자