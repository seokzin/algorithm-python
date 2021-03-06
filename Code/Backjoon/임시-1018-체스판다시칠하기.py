n, m = map(int, input().split())

arr = [] # 알파벳 체스판

for i in range(n):
  arr.append(list(map(str, input())))

def comp(arr, x, y):
  dif = arr # arr 복사. 차이값을 숫자로 드러내자. 매번 초기화 해야함.

  for i in range(x, x+8):
    for j in range(y, y+8):
      if (i+j) % 2 == 0: # 첫 블록 포함 띄엄띄엄
        dif[j][i] = 1 if arr[j][i] == 'W' else 0
      else: # 둘째부터 띄엄띄엄
        dif[j][i] = 1 if arr[j][i] == 'B' else 0

  dif_num = sum(sum(dif, []))

  print(min(dif_num, 64-dif_num))

for y in range(n-8):
  for x in range(m-8):
    comp(arr, x, y)

# 2d 리스트는 count, sum이 안된다. 2번 나눠야 한다. 대신 sum은 sum(sum(arr, []))로 가능