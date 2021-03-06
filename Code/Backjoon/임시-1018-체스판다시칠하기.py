n, m = map(int, input().split())

arr = [] # 체스판 담을 배열

for i in range(n):
  arr.append(input())

cnt = 0 # 틀린 무늬 카운트

# 아이디어: w = 0 b = 1로 치환해서 원본과 가본을 뺀다. 0을 카운트하거나 1, -1을 카운트한거의 min값을 채택한다.

# ex)시작 좌표 x, y
def compare(arr, x, y): 
  for i in range(x, x+8):
    if arr[(i%2 == 1)] == 'W':
      continue

# 1920번 어렵네. 나중에 다시 풀자