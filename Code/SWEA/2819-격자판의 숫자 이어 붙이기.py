D = ((0, -1), (0, 1), (-1, 0), (1, 0))


def dfs(x, y, s):
    if len(s) == 7:
        if s not in case:
            case.append(s)
        return
            
    for dx, dy in D:
        nx, ny = x+dx, y+dy

        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, s+arr[nx][ny])


for tc in range(1, int(input())+1):
    arr = [input().split() for _ in range(4)]
    case = []

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    print(f'#{tc}', len(case))