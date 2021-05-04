fac = [[0 for j in range(i+1)] for i in range(101)]

fac[0][0] = fac[1][0] = fac[1][1] = 1

for i in range(2, 101):
  for j in range(i+1):
    if i == j or j == 0:
      fac[i][j] = 1
    else:
      fac[i][j] = fac[i-1][j-1] + fac[i-1][j]

n, m = map(int, input().split())

print(fac[n][m])

# dp - 파스칼 삼각형을 통해 조합 구하는 방법. but 메모리, 시간 다 비슷했다.