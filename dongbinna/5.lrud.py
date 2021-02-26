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
    if plan == move_types[i]: # plan이 어떤 무브타입인지 체크해주는 장치
      nx = x + dx[i]
      ny = y + dy[i]
  
  if nx < 1 or ny < 1 or nx > n or ny > n:
    continue
  
  x, y = nx, ny # 벗어나지 않았다면 적용하기

print(x, y)

# 행렬상에서 dy가 가로가 된다..
# 어렵다. 15라인, 19라인의 위치와 의미를 다시금 복기하기
# 15 - plan의 알파벳과 방향벡터를 매칭
# 19 - 이동해보고 범위 벗어난지 체크 후 반영