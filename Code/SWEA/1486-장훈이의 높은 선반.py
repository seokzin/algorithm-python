def dfs(x, h):
    global res
    
    d = h-b

    if d >= res:
        return

    if x == n:
        if d >= 0:
            res = d
        return

    dfs(x+1, h+arr[x])
    dfs(x+1, h)


for tc in range(1, int(input())+1):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    res = float('inf')

    dfs(0, 0)
    
    print(f'#{tc}', res)
