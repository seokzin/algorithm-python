n, m = map(int, input().split())

def fac(n):
  if n == 1:
    return 1
  return n * fac(n-1)

print(fac(n) // (fac(m) * fac(n-m)))

# 난이도를 예상해 당연히 틀릴 줄 알았는데 맞아서 의문이었던 문제. 그래서 dp로도 다시 풀어봤다.