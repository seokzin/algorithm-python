x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y1) - (y2-y1)*(x3-x1)


if ccw(x1,y1,x2,y2,x3,y3) * ccw(x1,y1,x2,y2,x4,y4) < 0 and ccw(x3,y3,x4,y4,x1,y1) * ccw(x3,y3,x4,y4,x2,y2) < 0:
    print(1)
else:
    print(0)


# 세 점이 일직선에 없다는 조건을 주었지만, 이것까지 고려하면 원래 더 복잡해진다.
# ccw 개념을 응용하여, 선분이 교차한다면 2개의 삼각형 곱이 음수다.