import sys
sys.setrecursionlimit(10**6)

def dfs(x):
  global res

  visit[x] = 1
  cycle.append(x)
  number = arr[x]
  
  if visit[number]:
    if number in cycle: # 여기 거짓 사례 이해가 중요
      res += cycle[cycle.index(number):] # 사이클만 골라내기
    return
  else:
    dfs(number)

t = int(input())

for _ in range(t):
  n = int(input())
  arr = [0] + list(map(int, input().split())) # 인덱스 편하게 맞추기
  visit = [0] * (n+1)
  res = []
  
  for i in range(1, n+1):
    if not visit[i]: # visit = 0
      cycle = []
      dfs(i)
          
  print(n - len(res)) # 속하지 못한 학생 수

# 순열 사이클 + 마지막 노드는 첫 노드를 가리켜야 함
# 코드 이해는 되는데 직접 구현은 힘들겠다. 사이클 공부
# 재귀에러? 10**5 도 모자른건가.. 10**6으로 클리어