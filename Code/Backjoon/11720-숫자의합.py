while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break

# 몇개의 테스트 케이스가 주어졌는지 알 수 없기에 EOF까지 받으면 된다고 함.
# 정석: import sys 모듈을 통해