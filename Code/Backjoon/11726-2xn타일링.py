n = int(input())

dp = [0, 1, 2]

for i in range(3, n+1):
  dp.append(dp[i-2] + dp[i-1])

print(dp[n] % 10007)

# dp 테이블을 사용하지 않고 재귀함수로 풀자 시간초과 발생
# append와 dp 초기화를 미리 n+1개로 한것과 시간 메모리 차이는 거의 없다.