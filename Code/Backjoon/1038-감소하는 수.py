import sys

# sys.setrecursionlimit(10 ** 9)


def solve(n):
    cnt = 0
    num = 1

    while True:
        snum = str(num)
        flag = True

        if len(snum) == 1:  # 길이가 1이면 감소하는 수
            pass

        else:
            for i in range(1, len(snum)):
                if int(snum[i]) < int(snum[i - 1]):  # 감소하는 수
                    continue
                else:  # 감소수가 아니면 불필요 연산 올 패스
                    num = int(snum[:i-1] + str(int(snum[i-1]) + 1) + '0'*(len(snum)-i))  # 3220 -> 3300 으로 점프
                    flag = False
                    break

        if flag:
            cnt += 1

            if cnt == n:  # n번째 감소하는 수
                return num

            num += 1


n = int(input())

if n >= 1023:  # 1022: 9876543210
    print(-1)  # N번째 감소하는 수 x
elif n == 0:
    print(0)
else:
    print(solve(n))

# 1022번째가 마지막인걸 어떻게 알았을까?
# 아이디어는 그렇다 쳐도 구현이 마냥 쉽지는 않을 문제다