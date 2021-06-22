# 분할 정복, 2*2 까지 줄이자
n, r, c = map(int, input().split())

res = 0

while n > 1:
  if r < 2**(n-1):
    if c < 2**(n-1):
      #2사분면
      pass
    else:
      #1사분면
      c -= 2**(n-1)
      res += 1 * 2**(2*n-2)
  else: 
    if c < 2**(n-1):
      #3사분면
      r -= 2**(n-1)
      res += 2 * 2**(2*n-2)
    else:
      #4사분면
      r -= 2**(n-1)
      c -= 2**(n-1)
      res += 3 * 2**(2*n-2)

  n -= 1

if r == 0:
  if c == 0:
    print(res)
  else:
    print(res + 1)
else:
  if c == 0:
    print(res + 2) 
  else:
    print(res + 3)

# 결국 단순하게 생각한 방법이 맞았음
# 함수 지양하자
# 그림 추가해서 포스팅하자