def dfs(now,l,r):
  dif = abs(l-r)

  if visit[dif] == 0:
    visit[dif] = 1

  if now == n:
    return 0
    
  if dp[now][dif] == 0:
    # 저울의 왼쪽에 놓는경우
    dfs(now+1, l+n_list[now], r)

    # 저울의 오른쪽에 놓는경우
    dfs(now+1, l, r+n_list[now])

    # 저울에 아예 안놓는경우
    dfs(now+1, l, r)
    
    dp[now][dif] = 1
    
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

visit = [0] * 40001
dp = [[0]*40001 for _ in range(n+1)]


dfs(0, 0, 0)

for i in range(0, m):
  if(visit[m_list[i]] == 1):
    print("Y",end=' ')
  else:
    print("N",end=' ')

# visit과 dfs가 다 필요한가?
# visit가 내부에서 할당 가능할까?
# 문제 조건이 거지같다. 이거 문제 제대로 이해해서 다시 보자

## 단순 그리디 풀이도 먹히는 것 같다. 조건상