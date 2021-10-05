def dfs(x, y, s):
    global res

    if s >= res:
        return

    if x+y == 2*(n-1):
        res = s
        return

    if x < n-1:
        dfs(x+1, y, s+arr[y][x+1])
    if y < n-1:
        dfs(x, y+1, s+arr[y+1][x])


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = float('inf')

    dfs(0, 0, arr[0][0])
    
    print(f'#{tc}', res)