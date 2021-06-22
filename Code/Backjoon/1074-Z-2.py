n, r, c = map(int, input().split())

res = 0

while n > 0:
  h = 2**(n-1) # 리스트 길이의 절반

  if r > h-1:
    res += 2*h*h
    r -= h

  if c > h-1:
    res += h*h
    c -= h

  n -= 1

print(res)

# r와 c는 서로 연관이 없다는 점에 착안해 사분면 없이 풀었다.