import sys
input = sys.stdin.readline

n = int(input())
dp = [[0]*n for i in range(n)]  # dp[start][end]
num = list(map(int, input().split()))

for i in range(n):
  for start in range(n):
    end = start + i

    if end >= n:
      break

    if start == end:  # 길이=1 -> dp=1
      dp[start][end] = 1
      continue

    if start + 1 == end: # 길이=2 -> dp=1
      if num[start] == num[end]:
        dp[start][end] = 1
        continue
    if num[start]==num[end] and dp[start+1][end-1]:  # 처음=끝 and 이전dp=1
      dp[start][end] = 1

m = int(input())

for i in range(m):
  a, b = map(int, input().split())
  print(dp[a-1][b-1])

# 함수화가 어울릴 것 같다. 근데 실력 기르고 다시 리팩토링 해야할 듯
# DP를 활용하는 새로운 사례였다. 굿