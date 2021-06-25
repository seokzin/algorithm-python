n = int(input())
res = 0
s = [] 

def dfs(n):
  global res

  s.append(n) # 넣고 검증하고 DFS 할건데 여기서부터 멈춤

  idx = len(s)-1 # 자주 쓰여서 변수화

  if idx == n-1: # 끝까지 도달 성공시 +1
    res += 1
    return
  
  # 배치가능 검증
  if idx > 0:
    for j in range(idx):
      if s[-1] == s[j] or s[-1] == s[j]+idx-j or s[-1] == s[j]-idx+j:
        s.pop()
        return
    
    
    dfs(n)




    dfs()
    s.pop()

dfs()

# 2차원 배열을 visit으로 하는건 가장 단순무식한 방법
# 결국 가로는 상관없다. 윗놈의 좌중우만 피하면 되고 윗윗놈의 좌좌 중 우우만 피하면 된다.

# 함수는 global 없이 list에 접근할 수 있나?