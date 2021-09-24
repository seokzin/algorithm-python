def solve(cost, m):
    global res

    if m > 12:
        res = min(res, cost)
        return

    # 1일권, 1달권
    solve(cost + min(a*arr[m], b), m+1)

    # 3달권
    solve(cost + c, m+3)


for tc in range(1, int(input())+1):
    a, b, c, d = map(int, input().split())  # 1일, 1달, 3달, 1년
    arr = [0] + list(map(int, input().split()))
    res = d  # 1년치로 초기화

    solve(0, 1)
    
    print(f"#{tc} {res}")