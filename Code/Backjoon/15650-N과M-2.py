n, m = map(int, input().split())
s = []

def dfs(start):
  if len(s) == m:
    print(*s)
    return
  
  for i in range(start, n+1):
    # if i not in s:
    s.append(i)
    dfs(i+1)
    s.pop()

dfs(1)

# 15649와 비슷하니 묶어서 생각
# not in은 if visited와 비슷한 기능. 다만 중복 값은 동일 취급되는 단점이 있다.