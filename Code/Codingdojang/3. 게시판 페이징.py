# A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.

# 입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)
# 출력 : 총페이지수

# m	n	출력
# 0	1	0
# 1	1	1
# 2	1	2
# 1	10	1
# 1010	1
# 1110	2

# 내 아이디어: m 안에 n이 몇번 들어가는가? 몫의 개념 / 나머지 존재시 m ++
# 강의 아이디어: = 내 아이디어. but 코딩 이후 검증 작업을 거쳐 코드 간결화

# tip 1. 예외가 나오면 법칙을 생각해보자 (elif을 엄두)

def calcNumOfPages(m, n):
    # if m == 0:
    #     return 0 검토시 불필요 코드임을 알아냄
    if m % n > 0:
        return m // n + 1
    return m // n

print(calcNumOfPages(0, 1))
print(calcNumOfPages(1, 1))
print(calcNumOfPages(2, 1))
print(calcNumOfPages(1, 10))
print(calcNumOfPages(10, 10))
print(calcNumOfPages(11, 10))