# 행렬의 거듭제곱을 이용한 피보나치 구하기 방식

n = int(input())

mat = [[1, 1], [1, 0]] # 제곱될 행렬
res = [[1, 0], [0, 1]]

def multi(a, b):
  mul = [[0] * 2 for _ in range(2)] # 2x2 배열 초기화

  for i in range(2):
    for j in range(2):
      for k in range(2):
        mul[i][j] += a[i][k] * b[k][j]

  for i in range(2):
    for j in range(2):
      mul[i][j] %= 1000000007

  return mul
  
while n:
  if n % 2: # 나머지 1 일때 
    res = multi(res, mat) # 제곱수가 홀수일 때 분할을 통해 짝수로 만들어준다.
  mat = multi(mat, mat) 
  n //= 2 # 제곱 횟수를 log 복잡도로 줄이는 과정

print(res[1][0])

# 수학적 지식 - 피보나치를 행렬곱으로
# 센스 - (22~26)제곱을 log 복잡도로 줄이는 방법