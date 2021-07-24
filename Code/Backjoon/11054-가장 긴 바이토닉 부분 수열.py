n = int(input())
arr = list(map(int, input().split()))

dp_up = [1] * n # 길이 최소값 = 1
dp_down = [1] * n

for i in range(n):
  for j in range(i):
    if arr[i] > arr[j] and dp_up[i] <= dp_up[j]:
      dp_up[i] = dp_up[j]+1

for i in range(n-1, -1, -1):
  for j in range(n-1, i, -1):
    if arr[i] > arr[j] and dp_down[i] <= dp_down[j]:
      dp_down[i] = dp_down[j]+1

dp_total = [x+y for x, y in zip(dp_up, dp_down)]

print(max(dp_total)-1) # up과 down에 본인이 2번 들어가 있어서


"""
- 가장 긴 증가하는 부분 수열(LIS) 응용
- 어떻게 띄엄띄엄 수열까지 파악하느냐가 핵심 -> dp_up[i] <= dp_up[j]
- 리스트 요소끼리 더하기
  1. for문
  2. zip을 통해 리스트 2개 튜플로 묶기
  2-2. zip과 1줄 for문 응용 -> 이 방법 사용
"""
