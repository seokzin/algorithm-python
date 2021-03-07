n, m = map(int, input().split())

arr = []

result = 64 # 색칠할 최소값 64로 초기화

for i in range(n):
  arr.append(input())

for i in range(n-7):
  for j in range(m-7):
    cnt = 0
    for y in range(i, i + 8):
      for x in range(j, j + 8):
        if (y+x) % 2 == 0: # 2중 리스트의 체크무늬끼리는 인덱스 합의 홀짝이 같다.
          if arr[y][x] == 'B': 
            cnt += 1
        else: # (y+2) % 2 == 1
          if arr[y][x] == 'W':
            cnt += 1
        
    result = min(result, cnt, 64-cnt) # BWBW 체스판과 WBWB 체스판은 합이 64인 관계다. 따로 구할 필요가 없다.
    
print(result)

# 15-16) if문을 한줄로 합치면 어떤 문제가 생길까?