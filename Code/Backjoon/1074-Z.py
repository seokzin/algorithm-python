# 분할 정복, 재귀 호출 문제이다.
# 1. 주어진 배열을 4등분 한다. (분할 정복)
# 2. 1의 과정을 반복적으로 진행하면서 단위가 2*2일 때 탐색을 시작한다. (재귀 호출)
# 3. r, c를 탐색하면 출력하고 종료한다.
n, r, c = map(int, input().split())

target = 0

while n > 1:
  if r < 2**(n-1):
    if c < 2**(n-1):
      #2사분면
      pass
    else:
      #1사분면
      c -= 2**(n-1)
      target += 1 * 2**(2*n-2)
  else: 
    if c < 2**(n-1):
      #3사분면
      r -= 2**(n-1)
      target += 2 * 2**(2*n-2)
    else:
      #4사분면
      r -= 2**(n-1)
      c -= 2**(n-1)
      target += 3 * 2**(2*n-2)
  n -= 1

if r == 0:
  if c == 0:
    print(target)
  else:
    print(target + 1)
else:
  if c == 0:
    print(target + 2) 
  else:
    print(target + 3)

# 결국 단순하게 생각한 방법이 맞았음
# 함수 지양하자
# 그림 추가해서 포스팅하자