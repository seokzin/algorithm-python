# 테이블의 모든 요소에 최적값을 기록해야 한다.
for tc in range(int(input())): # test case
  n, m = map(int, input().split())
  array = list(map(int, input().split()))
  dp = [] # 2차원 dp테이블
  index = 0
  for i in range(n):
    dp.append(array[index: index+m])
    index += m
  # dp 진행
  for j in range(1, m):
    for i in range(n):
      if i == 0: left_up = 0
      else: left_up = dp[i-1][j-1] # 왼쪽 위에서 오는 경우
      if i == n-1: left_down = 0
      else: left_down = dp[i+1][j-1] # 왼쪽 아래에서 오는 경우
      left = dp[i][j-1] # 왼쪽에서 오는 경우
      dp[i][j] = dp[i][j] + max(left_up, left_down, left)

  result = 0
  for i in range(n):
    result = max(result, dp[i][m-1])
  
print(result)