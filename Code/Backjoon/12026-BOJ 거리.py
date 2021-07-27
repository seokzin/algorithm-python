def prev_pos(x):
  if x == 'B':
    return 'J'
  elif x == 'O':
    return 'B'
  elif x == 'J':
    return 'O'

n = int(input())
arr = list(input())
MAX = 1000001
dp = [MAX] * n # 1000**2 + 1 로 초기화
dp[0] = 0

for i in range(1, n):
  prev = prev_pos(arr[i])

  for j in range(i):
    if arr[j] == prev:
      dp[i] = min(dp[i], dp[j] + (i-j)**2)

print(dp[n-1] if dp[n-1] != MAX else -1)

# DP 문제
# prev_pos 함수를 따로 빼는게 더 효율적