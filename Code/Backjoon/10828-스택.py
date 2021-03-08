import sys

n = int(input())

stack = []

for i in range(n):
  cmd = sys.stdin.readline().split() # map까지 쓸 필요가 없다.

  if cmd[0] == 'push':
    stack.append(cmd[1])
  elif cmd[0] == 'pop':
    print(stack.pop() if stack else -1)
  elif cmd[0] == 'size':
    print(len(stack))
  elif cmd[0] == 'empty':
    print(1 if not(stack) else 0)
  else: # cmd == 'top'
    print(stack[-1] if len(stack) > 0 else -1)

# order -> cmd 명명 변경
# input().split() 자체로도 문자열을 리스트화 해줌. 굳이 list(map.split()) 쓸 필요가 없다.
# 시간초과 -> import sys
# remove는 같은 숫자에서 임의의 값을 지울 수도 있음. del은 인덱스 지정
# if len(stack) > 0 은 if stack로 대처 가능. not(stack)도 가능. list의 T F 조건 알아보기
# pop 메소드 - 마지막 인덱스 출력 및 삭제
