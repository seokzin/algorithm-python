T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0] *(N+1) for _ in range(N+1)]  # 0*0부터 X,Y 까지 넓이 가진 리스트
    dp_sum = []  # M*M 넓이 합들 담는 리스트

    for i in range(N):
        for j in range(N):
            dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + arr[i][j]
    
    for x in range(N+1-M):
        for y in range(N+1-M):
            dp_sum.append(dp[y+M][x+M] - dp[y+M][x] - dp[y][x+M] + dp[y][x])

    print(f"#{tc} {max(dp_sum)}")

# N이 매우 클 땐 일일히 구하면 시간 초과가 뜨기 때문에 미리 넓이를 DP로 계산하였습니다.
# SWEA 문제는 이렇게까지 안풀어도 패스일 것 같습니다.
# 참고로 12, 16 라인의 dp 연산은 사각형 넓이 구하기입니다. (백준: 11660)