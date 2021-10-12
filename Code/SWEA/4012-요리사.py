from itertools import combinations


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    res = float('inf')

    for a in combinations(range(n), n//2):
        b = tuple(set(range(n)) - set(a))  # B는 A의 여집합

        fa = fb = 0

        for x, y in combinations(a, 2):
            fa += arr[x][y] + arr[y][x]

        for x, y in combinations(b, 2):
            fb += arr[x][y] + arr[y][x]

        res = min(res, abs(fa-fb))

    print(f"#{tc} {res}")