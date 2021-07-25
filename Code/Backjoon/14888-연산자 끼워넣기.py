n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

dp = []

def dfs(i, res, add, sub, mul, div):
  if i == n:
    dp.append(res)
    return

  else:
    if add:
      dfs(i+1, res+a[i], add-1, sub, mul, div)
    if sub:
      dfs(i+1, res-a[i], add, sub-1, mul, div)
    if mul:
      dfs(i+1, res*a[i], add, sub, mul-1, div)
    if div:
      dfs(i+1, int(res/a[i]), add, sub, mul, div-1)

dfs(1, a[0], add, sub, mul, div)

print(max(dp))
print(min(dp))

"""
음수의 나눗셈
1. 100//-3 = -34 -> 음수 몫은 내림이 된다.
2. int(100/-3) -33 -> int()는 반올림이 아니라 소수자리 버림이다.

global max, min을 지양하기 위해 dp 리스트를 사용하였다.
"""