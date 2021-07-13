def shoelace(x1,y1,x2,y2,x3,y3): # 신발끈 공식
  return (x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)

n = int(input())

x, y = map(int, input().split())

info = []
for i in range(num - 1):
  info.append(list(map(int, input().split())))

tmp = 0
for i in range(num - 2):
  tmp += shoelace(x,y,info[i][0],info[i][1],info[i+1][0],info[i+1][1])

print(abs(tmp)/2)

# 너무 기하문제.. -> 외적과 관련 (신발끈 공식)
# 다시 이해해보자
