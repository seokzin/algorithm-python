x = int(input())

line = 1 # 층수

while x > line:
  x -= line
  line += 1

if line%2 == 0:
  a = x
  b = line-x+1
else:
  a = line-x+1
  b = x

print(a, '/', b, sep='')

# 나름 개선하고 보니 다른 블로거랑 풀이가 완전 똑같다.. 포스팅 안해야지