T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pascal = [[0, 1, 0]]  # 앞뒤에 0을 넣어 예외처리 과정을 없앰

    for i in range(2, N+1):
        line = []

        for j in range(i):
            line.append(pascal[-1][j]+pascal[-1][j+1])
        pascal.append([0] + line + [0])

    print(f'#{tc}')
    for line in pascal:
        print(*line[1:-1])

#  출력부에 0 제거