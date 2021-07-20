n = int(input())

for _ in range(n):
  m = int(input())

  arr = []
  for i in range((m//10)+1):
    arr.extend(list(map(int,input().split())))

  mid = []

  for i in range(1, m+1, 2):
    mid_idx = i//2
    mid.append(sorted(arr[:i])[mid_idx])

  print((mid_idx)+1)

  for i in range((mid_idx//10)+1):
    print(*mid[10*i:10*(i+1)])

# extend -> 리스트에 내용물만 추가하는 방법
# 의도가 O(n^2) 쓰지 말란 것 같은데.. 문제가 아쉽다.