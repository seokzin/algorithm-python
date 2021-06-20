n = int(input())
a = [] # [키, 몸무게] 담은 리스트

for _ in range(n):
  a.append(input().split()) 

for i in a:
  rank = 1 # 등수 초기값

  for j in a:
    if j[0]>i[0] and j[1]>i[1]:
      rank += 1
  
  print(rank, end=' ')

# 사소한 변수 선언이 어렵다. a 명명..
# j가 본인까지 탐색하는 허술함이 있다. 복잡한 문제였다면 바껴야할 부분