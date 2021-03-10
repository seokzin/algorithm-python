import sys

n = int(input())

s = set()
s_all = set(map(str, range(1, 21))) # 최초 선언후 관리가 효율적

for i in range(n):
  cmd = sys.stdin.readline().split() # map까지 쓸 필요가 없다.

  if cmd[0] == 'add':
    s.add(cmd[1])
  elif cmd[0] == 'remove':
    s.discard(cmd[1])
  elif cmd[0] == 'check':
    print(1 if cmd[1] in s else 0)
  elif cmd[0] == 'toggle':
    s.discard(cmd[1]) if cmd[1] in s else s.add(cmd[1])
  elif cmd[0] == 'all':
    s = s_all
  else: # empty
    s = set()

# set remove는 요소 없으면 KeyError. discard는 요소 없어도 정상 작동
# i for i in range(20)의 type은 generator고 range(20)의 type은 range다. 바로 넣어줄땐 range 가 빠르지만 미리 선언을 하고 대입을 할땐 generator 가 빠르다. https://www.acmicpc.net/board/view/57656
# 6, 20) 동일한 생성자를 반복해서 호출하지 말자.