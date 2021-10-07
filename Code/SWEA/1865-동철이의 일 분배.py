def dfs(x, p, visit):
    global res

    if p <= res:
        return

    if visit == (1<<n) - 1:
        res = p
        return

    for i in range(n):
        if not visit & (1<<i):
            dfs(x+1, p * arr[x][i]/100, visit|(1<<i))


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = 0

    dfs(0, 1, 0)
    print(f'#{tc} {res*100:.6f}')