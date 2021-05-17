n, m = map(int, input().split())
li = sorted(list(set((list(map(int, input().split())))))) # 줄나눔이 가독성은 훨씬 좋은데 연습겸 한번에.. 효율은?
s = []

def dfs(start):
  if len(s) == m:
    print(*s)
    return
  
  for i in range(start, len(li)):
    s.append(li[i])
    dfs(i)
    s.pop()

dfs(0)