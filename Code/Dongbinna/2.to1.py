# 1 만들기
# 1. k씩 나누기 2. 1씩 빼기
# 빼기는 나누기 속도를 따라잡지 못한다.

# n, k를 공백을 기준으로 구분하여 입력받기
n, k = map(int, input().split())

result = 0

while True:
  target = (n//k) * k
  result += (n - target)
  n = target

  if n < k:
    break

  result += 1
  n //= k

result += (n-1)

print(result)

# 단순하게 짤 수도 있지만 이런 반복문으로 하면 log 복잡도로 줄일 수 있다. 일종의 테크닉