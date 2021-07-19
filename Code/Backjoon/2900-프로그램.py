import sys
input = sys.stdin.readline

n, k = map(int,input().split())
x_list = list(map(int,input().split()))
q = int(input())

# x를 압축함 -> 효율성
x_zip = [0] * n
for x in x_list:
  x_zip[x] += 1

# 배열을 구함
dp = [x_zip[1]] * n # x=1 일때는 미리 빼둠
dp_sum = [0] * (n+1)

for x in range(2, n):
  for i in range(0, n, x):
    dp[i] += x_zip[x]

# 배열의 부분합 구함
dp_sum[1] = dp[0]
for i in range(1, n):
  dp_sum[i+1] = dp_sum[i] + dp[i]

# 출력
for _ in range(q):
  l,r = map(int,input().split())
  res = dp_sum[r+1]-dp_sum[l]

  print(res)

# 큰 복잡도만 따지는게 아니라 n^2이 몇배까지 허용되는지 따져야 하는 효율성 관리 고난도 문제
# 결국 x_list의 최적화가 핵심인듯