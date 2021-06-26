import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = sys.maxsize

s = [[INF] * n for _ in range(n)]

for _ in range(m):
  a, b, w = map(int, input().split())
  s[a-1][b-1] = min(w, s[a-1][b-1]) # 여러 노선중 최소값을 넣는다

for k in range(n): # 경유지
  for i in range(n):
    for j in range(n):
      if i == j: # 출발-도착 같으면 0으로 초기화
        s[i][j] = 0 
      else:
        s[i][j] = min(s[i][j], s[i][k]+s[k][j])

# INF를 0으로 변환 - 출력부와 일부러 분리
for i in range(n):
  for j in range(n):
    if s[i][j] == INF:
      s[i][j] = 0

for l in s:
  print(*l)

# 플로이드 워셜 알고리즘 - 경유지의 for문을 통해 모든 경로를 파악한다. 거리 갱신이 누적값으로 계속 일어나니까
# 경유지가 첫번째가 되어야만 모든 케이스를 다 검증하게 된다!
# 출력부가 심플해서 포스팅 가치 O.. 라고 하기엔 INF->0부가 거슬리긴 한다.