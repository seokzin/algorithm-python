def dp(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  else:
    return dp(n-3) + dp(n-2) + dp(n-1)

for _ in range(int(input())):
  n = int(input())
  print(dp(n))

# for문을 통해 dp테이블에 n=10까지 값을 모두 구한 풀이도 있지만 확장성을 고려하면 안좋지않을까?