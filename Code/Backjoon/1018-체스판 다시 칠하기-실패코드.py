n, m = map(int, input().split())

arr = [] # 체스판

for i in range(n):
  arr.append(list(map(str, input())))

def comp(arr, x, y):
  dif = [[0] * 8] * 8 # 원본과 다른 부분을 1로 표시하는 체스판

  for i in range(x, x+8):
    for j in range(y, y+8):
      if (i+j) % 2 == 0: # 첫 블록 포함 띄엄띄엄
        dif[j-y][i-x] = 1 if arr[j][i] == 'W' else 0
      else: # 둘째부터 띄엄띄엄
        dif[j-y][i-x] = 1 if arr[j][i] == 'B' else 0

  print(dif)

  dif = [[0] * 8] * 8 # 다시 초기화
  dif_num = sum(sum(dif, []))

  print(min(dif_num, 64-dif_num))

for y in range(n-7):
  for x in range(m-7):
    comp(arr, x, y)

# 2d 리스트는 count, sum이 안된다. 2번 나눠야 한다. 대신 sum은 sum(sum(arr, []))로 가능
# 잔머리 굴리다 너무 복잡해진 케이스. 코드를 줄이는게 최선이 아니다. 가독성이 최선이다.
# dif 배열 대신 cnt를 도입하는게 더 좋았다.
# 함수가 아닌 for문으로 한번에 처리하는게 여기선 더 좋았다.