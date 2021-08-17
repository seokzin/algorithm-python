T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 가로 탐색
    for y in range(N):
        for x in range(N-M+1):
            row = arr[y][x:M+x]  
            
            if row == row[::-1]:  
                print(f"#{tc}", row)

    # 세로 탐색
    for y in range(N-M+1):
        for x in range(N):
            col = []
            for i in range(M):
                col.append(arr[y+i][x])

            if col == col[::-1]:  
                print(f"#{tc} ", *col, sep='')

# 회문1은 전치행렬 없이 인덱싱으로 풀었습니다.
# 회문2는 전치행렬을 사용해봤습니다. 확실히 편합니다.