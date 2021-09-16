n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n+1)  # '연속'된 증가수열 개수

for x in arr:
    dp[x] = dp[x-1]+1

print(n - max(dp))

# 연속 증가수열이 최대인 케이스에서 바꿔야 최소 교체