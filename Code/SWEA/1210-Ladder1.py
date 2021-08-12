for tc in range(10):
    T = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]  # 양측에 0 넣어 index out 방지

    x, y = arr[99].index(2), 99

    while True:
        y -= 1

        if arr[y][x-1]:  # 좌 갈림길
            while arr[y][x-1]:
                x -= 1
        elif arr[y][x+1]:  # 우 갈림길
            while arr[y][x+1]:
                x += 1
        elif y == 0:
            break

    print(f"#{T} {x-1}")