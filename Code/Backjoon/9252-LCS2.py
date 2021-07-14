a = [0] + list(input())
b = [0] + list(input())

len_a = len(a)
len_b = len(b)

dp = [[""]*len_b for _ in range(len_a)]

for i in range(1, len_a):
  for j in range(1, len_b):
    if a[i] == b[j]:
      dp[i][j] = dp[i-1][j-1] + a[i]
    else:
      if len(dp[i - 1][j]) > len(dp[i][j - 1]):
        dp[i][j] = dp[i-1][j]
      else:
        dp[i][j] = dp[i][j-1]

print(len(dp[len_a-1][len_b-1]))
print(dp[len_a-1][len_b-1])

# 9252
# 하나씩 당겨 나오는 이유 찾아보기
# DP 다시 실행해보기