while True:
  n = int(input())
  cnt = 0

  if n == 0:
    break
  
  for i in range(n+1, 2*n+1):
    if i == 2 or i == 3:
      cnt += 1
    else:
      root = int(i**0.5)
      
      for j in range(2, root+1):
        if i%j == 0:
          break
        elif j == root:
          cnt += 1

  print(cnt)

# 또 PyPy에서만 맞았다 ㅡㅡ