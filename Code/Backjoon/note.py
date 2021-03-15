a, b, c = map(int, input().split())

# 1000 + 70x < 170x  a/(c-b) < x 되는 순간 탈출
if b >= c:
  print(-1)

else:
  print(a//(c-b) + 1)