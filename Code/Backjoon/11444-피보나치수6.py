n = int(input())
mat = [[1, 1], [1, 0]]
res = [[1, 0], [0, 1]]

def multi_mat(a, b):
  mul = [[0] * 2 for _ in range(2)]

  for i in range(2):
    for j in range(2):
      for k in range(2):
        mul[i][j] += a[i][k] * b[k][j]

  for i in range(2):
    for j in range(2):
      mul[i][j] %= 1000000007

  return mul
  
while n:
  if n & 1: 
    res = multi_mat(res, mat)
  mat = multi_mat(mat, mat)
  n //= 2

print(res[1][0])

# 20) 무슨 문법?