from collections import deque

v = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(v):
  path = list(map(int, input().split()))
  for i in range(1, len(path) - 2, 2): # 3번째 인수: 간격
    graph[path[0]].append((path[i], path[i + 1]))

max_dis = 0 # 최대거리
max_index = 0 # 최대거리의 노드

def bfs(n):
  global max_dis # 전역 변수를 로컬 범위에서 쓰는 방법
  global max_index

  # visit = dis = [0] * (v + 1) # 이러면 얕은복사 된다!!! 주의
  visit = [0] * (v + 1)
  dis = [0] * (v + 1)

  q = deque()
  q.append(n)
  visit[n] = 1

  while q:
    t = q.popleft()
    for i, d in graph[t]:
      if not visit[i]:
        visit[i] = 1
        dis[i] = dis[t] + d
        q.append(i)
        if max_dis < dis[i]:
          max_dis = dis[i]
          max_index = i

bfs(1) # 시작 노드는 자유
bfs(max_index) # 여기서 지름 거리 구해짐

print(max_dis)


# 아이디어: 노드 x에서 가장 거리가 먼 노드가 지름 중 한쪽이 된다. 거기서 최장거리 노드를 뽑으면 지름이 된다.
# L8-9: 구조분해할당 가능할까?
# 생각보다 용어 정리가 어렵다. 단어 단위로 써야하나? 아님 약어? 가독성은 뭐가 더 좋을지?
# L22: 리스트 속 리스트는 이런 식으로 출력 가능?
# L17-18: 명명이 적절할까? 2단어 명명은 언더바가 맞나?

# 파이썬 스코프 - if 바깥에서는 접근 가능, 함수 밖에서는 불가능
# visit에 dis 역할을 더하는게 낫나? 따로 분리하는게 낫나?..... 심미적으로