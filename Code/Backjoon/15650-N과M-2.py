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
# not in은 if visited와 비슷한 기능하는 괜찮은 문법인듯. 다만 여기선 안써도 결과 같음