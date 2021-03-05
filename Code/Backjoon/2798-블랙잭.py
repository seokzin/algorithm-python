n, m = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))

result = 0

for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      if arr[i] + arr[j] + arr[k] <= m:
        result = max(arr[i] + arr[j] + arr[k], result)

print(result)

# 8-9) 완전탐색 3중 for문의 범위를 제대로 설정하자. 