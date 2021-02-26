# 그리디 : 1~4

n = 1260
count = 0

# 큰 단위 화폐부터
array = [500, 100, 50, 10]

for coin in array:
  count += n // coin
  n %= coin

  print(count)

  # O(K) = n에 상관없이 화폐 계수 K에만 영향 받음.