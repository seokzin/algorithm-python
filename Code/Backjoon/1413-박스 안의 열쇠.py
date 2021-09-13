import math

n, m = map(int, input().split())
dp = [[0] * (n+1) for _ in range(n+1)]

dp[1][1] = 1

for i in range(2, n+1):
    for j in range(1, i+1):  # j = 상자 인덱스
        dp[i][j] = dp[i-1][j-1] + (i-1)*dp[i-1][j]  # 맨뒤에 추가(1개) + 중간에 추가(i개)

get = 0  # 열쇠 얻는 경우 / 총 경우

for i in range(1, m+1):
    get += dp[n][i]

total = math.factorial(n)  # 총 경우

gcd = math.gcd(get, total)  # 약분

print(f'{get//gcd}/{total//gcd}')

# DP식 생각하는건 수학적이라 어려웠다.