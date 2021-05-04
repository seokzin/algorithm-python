n = int(input())
seq = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
  for j in range(i):
    if seq[i] > seq[j]:
      # 핵심. max 속 dp[i]는 증가하지만 연속하지 않는 것들 걸러주는 장치 
      dp[i] = max(dp[i], dp[j]+1) 

print(max(dp))

# [0] * n 과 [0 range] 는 레퍼런스의 차이가 있다?
# range0은 그냥 pass라 봐야겠찌 에러 없이?