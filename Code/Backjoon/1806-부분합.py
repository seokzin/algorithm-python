n, s = map(int, input().split())
a = list(map(int, input().split()))
sum_part = [0] * (n+1)

# 부분합 채우기
for i in range(1, n+1):
  sum_part[i] = sum_part[i-1] + a[i-1]
    
# 투포인터 설정
res = 100_000 # 최대값으로 초기화
start = end = 0

while start != n:
  if sum_part[end] - sum_part[start] >= s:
    if end-start < res:
      res = end-start
    start += 1
        
  else:
    if end != n:
      end += 1
    else:
      start += 1

print(res if res<100000 else 0)

# 투포인터 알고리즘의 기초