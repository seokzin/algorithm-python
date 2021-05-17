n, m = map(int, input().split())
li = sorted(list(map(int, input().split()))) # 입력값 넣는 li
s = []

def dfs(start):
  if len(s) == m:
    print(*s)
    return
  
  for i in range(start, n):
    s.append(li[i])
    dfs(i)
    s.pop()

dfs(0)

# 베이스: N과M(4)