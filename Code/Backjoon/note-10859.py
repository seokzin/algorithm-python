n, m = map(int, input().split())

train = [[0]*20 for _ in range(n+1)]

# 명령수행
for _ in range(m):
  cmd = list(map(int, input().split()))
  
  i = cmd[1]

  if cmd[0] == 1:
    x = cmd[2]
    train[i][x-1] = 1
  elif cmd[0] == 2:
    x = cmd[2]
    train[i][x-1] = 0
  elif cmd[0] == 3:
    for x in range(19,0,-1):
      train[i][x] = train[i][x-1]
    train[i][0] = 0
  elif cmd[0] == 4:
    for x in range(19):
      train[i][x] = train[i][x+1]
    train[i][19] = 0

# 탐색
total = 0

train_dic = {}

for train in train:
    temp = map(str, train)
    temp_key = ''.join(temp)

    if temp_key not in train_dic:
        train_dic[temp_key] = 1
        total += 1

print(total)