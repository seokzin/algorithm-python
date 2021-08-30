x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
A, B, C, D = (x1,y1), (x2,y2), (x3,y3), (x4,y4)


def ccw(a,b,c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])


if ccw(A,B,C)*ccw(A,B,D) <= 0 and ccw(C,D,A)*ccw(C,D,B) <= 0:
    if ccw(A,B,C)*ccw(A,B,D) == 0 and ccw(C,D,A)*ccw(C,D,B) == 0:  # 평행할 때
        if (max(A[0],B[0]) >= min(C[0],D[0]) and  max(C[0],D[0]) >= min(A[0],B[0])) and (max(A[1],B[1]) >= min(C[1],D[1]) and max(C[1],D[1]) >= min(A[1],B[1])):  # 접하는지 확인
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)


# 세 점이 일직선에 없다는 조건을 주었지만, 이것까지 고려하면 원래 더 복잡해진다.
# ccw 개념을 응용하여, 선분이 교차한다면 2개의 삼각형 곱이 음수다.