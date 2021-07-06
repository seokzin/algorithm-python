import sys
sys.setrecursionlimit(10**5)


def dfs(x):
  global res
  visit[x] = True
  cycle.append(x)
  number = numbers[x]
  
  if visit[number]:
    if number in cycle:
      res += cycle[cycle.index(number):]
    return
  else:
    dfs(number)


for _ in range(int(input())):
  N = int(input())
  numbers = [0] + list(map(int, input().split()))
  visit = [True] + [False] * N #방문 여부
  res = []
  
  for i in range(1, N+1):
    if not visit[i]: #방문 안한 곳이라면
      cycle = []
      dfs(i) #DFS 함수 돌림
          
  print(N - len(res))