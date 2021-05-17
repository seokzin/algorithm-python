n, m = map(int, input().split())
s = []

def dfs():
  if len(s) == m:
    print(*s)
    return
  
  for i in range(1, n+1):
    if i not in s:
      s.append(i)
      # print('일', s)
      dfs()
      # print('이', s)
      s.pop()
      # print('삼', s)

dfs()

# 백트래킹?
# *list 문법 자세히는 모르겠지만 괄호 없이 출력해주는 문법같음
# 지금 보니 함수 속 파라미터랑 전역 변수랑 겹친 적이 있는 것 같음(n 등등..) 신경쓰자
# s.pop 이유 - print(s)로 시각화 가능. 모든 경우의 수 출력 위해 한칸씩 나아감
# dfs 깊이 n의 의미. n번째 요소를 이동시킬 것이다. 그림으로 그려봤을 때 이해했다. 