x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

d = (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)

if d > 0:
    print(1)
elif d < 0:
    print(-1)
else:
    print(0)

# 삼각형의 면적 공식을 활용한 벡터 문제
# https://www.acmicpc.net/blog/view/27