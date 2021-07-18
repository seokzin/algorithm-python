n, k = map(int, input().split())
arr = []
dp = [0 for _ in range(k+1)]

for _ in range(n):
  w, v = map(int, input().split())
  arr.append([w, v])

for i in range(n):
  i_w, i_v = arr[i][0], arr[i][1]

  for j in range(k, 0, -1):
    if j >= i_w:
      dp[j] = max(dp[j], dp[j-i_w]+i_v)

print(dp[-1]) # 마지막 값 = 최대

# 배낭 알고리즘 - 2중 DP
# 12865 배낭 문제와 똑같다. 하지만 리팩토링 한번 거쳐보기