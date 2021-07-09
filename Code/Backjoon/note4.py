# 9252

a = input()
b = input()

len_a = len(a)
len_b = len(b)

dp = [[""]*(len_a+1) for _ in range(len_b+1)]

for i in range(1, len_a):
  for j in range(1, len_b):
    if a[i] == b[j]:
      dp[i][j] = dp[i-1][j-1] + a[i]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(len(dp[len_a-1][len_b-1]))
print(dp[len_a-1][len_b-1])

# 하나씩 당겨 나오는 이유 찾아보기