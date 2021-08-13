T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    res = 0

    for _ in range(N):
        x1, y1, x2, y2, c = map(int, input().split())
        
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                arr[y][x] += c

    for row in arr:
        res += row.count(3)  # 보라색 카운팅

    print(f"#{tc} {res}")