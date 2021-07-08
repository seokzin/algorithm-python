n, s = map(int, input().split())
a = list(map(int, input().split()))

#0~n까지 합
_sum = [0] * (n+1)
for i in range(1, n+1):
  _sum[i] = _sum[i-1] + a[i-1]  
    
# 투포인터 설정
res = 1000001
start = 0
end = 1

while start != n:
  if _sum[end] - _sum[start] >= s:
    if end - start< res:
      res = end - start
    start += 1
        
  else:
    if end != n:
      end += 1
    else:
      start += 1

if res != 1000001:
  print(res)
else:
  print(0)

# 투포인터 or 부분합 둘다 풀어보기