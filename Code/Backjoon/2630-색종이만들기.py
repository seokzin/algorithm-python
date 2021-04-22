# 분할 정복 - 쿼드트리 (4개씩 나뉨)
def div(x, y, n):
  global blue, white
  color = matrix[y][x] # 첫 색깔과 나머지 색이 같아야함
    
  for i in range(x, x+n):
    for j in range(y, y+n):
      if matrix[j][i] != color: # 하나라도 틀릴시에 재귀문 생성
        div(x, y, n//2) # 2사분면
        div(x + n//2, y, n//2) # 1사분면
        div(x, y + n//2, n//2) # 3사분면
        div(x + n//2, y + n//2, n//2) # 4사분면
        return
    
  if color == 0: # 모두 흰색
    white += 1
    return
  else:
    blue += 1
    return

n = int(input())
matrix = []

blue = 0
white = 0

for _ in range(n):
  matrix.append(list(map(int, input().split())))

div(0, 0, n)
print(white)
print(blue)

# 함수 속 글로벌?
# 리턴의 존재 이유를 곱씹어보자.