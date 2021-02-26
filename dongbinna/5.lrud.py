# 상하좌우 - 좌표 벗어나면 움직임 무시

n = int(input())
x, y = 1, 1
plans = input().split()

# L R U D 이동 벡터
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

move_types = ['L', 'R', 'U', 'D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  
  x, y = nx, ny

print(x, y)

# 행렬상에서 dy가 가로가 된다..
# 어렵다. 왜 위치 벗어남 확인이 19라인에 있으며 15줄 if문의 의미는 무엇인가?