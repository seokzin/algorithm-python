t = int(input())

for i in range(t):
  r, s = input().split(' ')
  for j in range(len(s)):
    print(int(r) * s[j], end = '') # 
  print() # 다음 입력 위한 줄바꿈


# 다 입력 받고 한 번에 출력이 아닌 1줄 입력 - 1줄 출력이 된다는 소리..?