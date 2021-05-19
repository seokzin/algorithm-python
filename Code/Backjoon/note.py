n = int(input())

if n < 2:
  print(n)
else:
  x, y = 0, 1

  for _ in range(2, n+1):
    x, y = y, x+y
  
  print(y % 1000000007)