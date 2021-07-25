def fac(n):
  num = 1
  for i in range(1, n+1):
    num *= i
  return num


t = int(input())

for _ in range(t):
  n, m = map(int, input().split())

  res = fac(m) // (fac(n) * fac(m - n)) # 조합 공식
  
  print(res)