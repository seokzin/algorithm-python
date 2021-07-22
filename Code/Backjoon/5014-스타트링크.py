from collections import deque

def bfs():
  q = deque()
  q.append(s)

  steps = [0] * (f+1) # visit + steps 기능
  steps[s] = 1 # s = g 일 때와 답이 없을때를 구분하기 위해 초기값 1

  while q:
    x = q.popleft()

    for nx in (x+u, x-d):
      if 0 < nx <= f and steps[nx] == 0:
        steps[nx] = steps[x]+1
        q.append(nx)

  if steps[g] == 0:
    return 'use the stairs'
  
  return steps[g]-1

f, s, g, u, d = map(int, input().split())

print(bfs())

# visit 값끼리 대소 비교 안하는 이유 -> BFS기 때문에 나중에 들어온 값이 무조건 크다
# 알고리즘은 쉬운데 예외 처리가 조금 까다로웠다.