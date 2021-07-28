from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
trains = [deque([0]*20) for _ in range(n)]
res = []  # 중복 아닌 기차만 담을 리스트

for _ in range(m):
  cmd = list(map(int,input().split()))

  if cmd[0] == 1:
    trains[cmd[1]-1][cmd[2]-1] = 1

  elif cmd[0] == 2:
    trains[cmd[1]-1][cmd[2]-1] = 0

  elif cmd[0] == 3:
    trains[cmd[1]-1].rotate(1)
    trains[cmd[1]-1][0] = 0

  else:
    trains[cmd[1]-1].rotate(-1)
    trains[cmd[1]-1][19] = 0

for train in trains:
  if train not in res:
    res.append(train)

print(len(res))

# deque.rotate()를 처음 다뤄본 문제 (구글 참고)