import sys

input = sys.stdin.readline
INF = sys.maxsize # 2^63 - 1

def bf():
  # 최단 경로 길이는 최대 n-1이다. n번째는 음의 사이클 체크 용도
  for times in range(n):
    for v in range(1, n+1):
      for nv, nw in graph[v]:
        if dis[nv] > dis[v] + nw:
          dis[nv] = dis[v] + nw
          if times == n-1: # n-1회에도 dis가 갱신됐다면 음의 사이클 존재 증거 
            print("YES")
            return
  print("NO")
  return

tc = int(input())

for _ in range(tc):
  n, m, w = map(int, input().split())
  dis = [INF] * (n + 1)
  graph = [[] for _ in range(n + 1)]

  for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])
    graph[e].append([s, t])
    
  for _ in range(w):
    s, e, t = map(int, input().split())
    graph[s].append([e, -t])

  bf()

# 벨만포드 알고리즘 - 음수 간선이 있을 때 최단 거리 문제. 출발 노드 필요
# 또한 알고리즘을 2번 돌려서 음수 간선의 순환도 체크할 수 있다.
# O(VE)로 다익스트라보다 느리다. 전체 간선에 대해 업데이트 발생하기 때문
# 문제의 의도: 음의 사이클이 존재하냐 안하냐?
# 이번 문제의 변수 명명 방식이 맘에 든다. nw, nv..