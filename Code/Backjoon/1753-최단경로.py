import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize # 9223372036854775807

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v + 1)] 
dp = [INF] * (v + 1)
heap = []

for _ in range(e):
  u, v, w = map(int, input().split())
  graph[u].append([v, w])

def dijkstra(start):
  dp[start] = 0
  heapq.heappush(heap, [0, start]) # heappop 최소값을 위해 w, n 순으로 넣어준다..?

  while heap:
    now_w, now = heapq.heappop(heap)

    for new, new_w in graph[now]: # 전역과 지역 중복해도 가독성 좋을까? 
      cal_w = now_w + new_w
      
      if cal_w < dp[new]:
        dp[new] = cal_w
        heapq.heappush(heap, [cal_w, new])

dijkstra(k)

for i in dp[1:]:
  print(i if i != INF else "INF")

# 다익스트라 알고리즘 - 하나의 정점에서 나머지 모든 정점까지의 최단거리
# 푸시 인자로 tuple과 list의 차이..
# sys.maximize - 정수 최대값 - 2^63 - 1
# 함수 선언 뒤에 인수 초기화 오는게 낫나?
# 대문자 변수 - 상수 표현 규칙 / 대문자 함수는 무슨 의미..?
# (wei, idx) 순으로 넣는 이유..? - heappop이 wei 기준으로 일어나게 하려고? 그럼 2, 3 이 들어가면 어떻게 정렬되지?
# wei가 3개씩 등장하니 명명이 가장 어려웠다. 수식어는 앞이 맞는건가?