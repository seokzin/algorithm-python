# 1463 - 3으로 나누는게 최적을 보장하지 않는다. ex) 10

n = int(input())

cnt = 0

while n > 1:
  if n % 3 == 0:
    n = n//3
    cnt += 1
  elif n % 2 == 0:
    n = n//2
    cnt += 1
  else:
    n = n-1
    cnt += 1

print(cnt)