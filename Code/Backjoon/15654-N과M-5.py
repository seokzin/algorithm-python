n, m = map(int, input().split())
li = sorted(list(map(int, input().split()))) # 입력값 넣는 li
s = [] # 수열 출력을 위한 li

def dfs():
  if len(s) == m:
    print(*s)
    return
  
  for i in li:
    if i not in s:
      s.append(i)
      dfs()
      s.pop()

dfs()

# 15649의 응용. 정렬만 먼저 잘 해주자. 근데 li와 s를 따로 두는게 최선이겠지?