# 아이디어 : LIS(Longest Increasing Subsequence) 가장 긴 증가하는 부분수열
# D(i) = max(D[i], D[j]+1) if array[j] < array[i]
n = int(input())
array = list(map(int, input().split()))
array.reverse() # LIS 문제 형태로 변환

dp = [1] * n # DP 테이블 초기화

# LIS 알고리즘
for i in range(1, n):
  for j in range(0, i):
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j] + 1)

# 열외할 병사의 최소 수 출력
print(n - max(dp))