DELTA = ((1, 0), (0, 1), (-1, 0), (0, -1))  # 우-하-좌-상 순서

def move():
    x, y = 0, 0
    num = 2  # 2부터 시작
    visit[y][x] = 1

    for d in range(2*N - 1):  # 방향 전환은 2N-1 회 발생
        dx, dy = DELTA[d%4]  # 방향 전환 사이클을 위해 % 사용

        while True:  # 값이 1이다 = 아직 방문하지 않았다.
            if 0 <= x+dx < N and 0 <= y+dy < N and visit[y+dy][x+dx] == 0:
                x, y = x+dx, y+dy
                arr[y][x] = num
                num += 1
                visit[y][x] = 1

                if num > N ** 2:  # 마지막 번호일 때 탈출
                    return
            else:  # 범위 벗어나거나 이미 방문했을 때 break를 하여 방향 전환
                break


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[1]*N for _ in range(N)]  # 시작점 값인 1로 초기화
    visit = [[0]*N for _ in range(N)]

    move()

    print(f'#{tc}')
    for row in arr:
        print(*row)
