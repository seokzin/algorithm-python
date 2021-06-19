t = int(input())

for _ in range(t):  
  k = int(input()) # 층
  n = int(input())  # 호

  res = [i for i in range(1, n+1)]  # 0층 결과로 초기화

  for _ in range(k):  # 층 만큼 반복하며 res에 값 누적
    for i in range(1, n):
      res[i] += res[i-1]  # 핵심: 아래 i-1층까지의 합이 res[i-1]과 같음을 알자.

  print(res[-1])