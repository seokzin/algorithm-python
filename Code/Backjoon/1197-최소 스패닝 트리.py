import sys
input = sys.stdin.readline

def union(a, b):  # 사이클 검토
  a = find(a)
  b = find(b)

  if b < a:
    parent[a] = b
  else:
    parent[b] = a

def find(a):  # 간선들이 이은 두 정점 찾기
  if a == parent[a]:
    return a

  parent[a] = find(parent[a])  # 경로 압축
  return parent[a]

v, e = map(int, input().split())
graph = []
parent = list(range(v+1))
cost = 0

for _ in range(e):
  a, b, c = map(int, input().split())
  graph.append((c, a, b))

graph.sort()  # 인덱스[0]=가중치 기준으로 정렬.. 아마?

for w, s, e in graph:
  if find(s) != find(e):
    union(s, e)
    cost += w

print(cost)

# 2차원 리스트에 그냥 sort()를 하면 어떤 기준으로 정렬될까?
# 크루스칼 코드가 잘 이해 안된다... 다음에 한번 다시 보자