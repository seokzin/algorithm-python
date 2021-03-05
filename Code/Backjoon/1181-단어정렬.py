n = int(input())

arr = []
result = []

for i in range(n):
  arr.append(input())

arr.sort()

for i in range(1, 51):
  for j in arr:
    if len(j) == i and j not in result:
      result.append(j)

for i in result:
  print(i)

# set은 순서 유지 및 정렬 X. if not in arr를 통해 중복 제거 해야함. 또는 list(set)을 거쳐서 중복 제거한 리스트로 만든다.