import sys

def dfs(idx):
  num = ""

  if idx == len(arr):
    print(*res)
    sys.exit() # 1개만 출력

  for i in range(idx, idx+2):
    if i >= len(arr): # 없앨 수 있을 것 같은데..
      continue
    num += arr[i]

    if (int(num)) > n or visit[int(num)]: 
      continue

    visit[int(num)] = 1
    res.append(int(num))
    dfs(i+1)
    visit[int(num)] = 0 # 백트래킹 과정
    res.pop()

arr = input()
res = []
n = 9 + (len(arr)-9)//2 ## 자릿수로 n 예측
visit = [0] * (n+1)

dfs(0)

# 백트래킹 + DFS
# 실1치곤 좀 난이도 있다