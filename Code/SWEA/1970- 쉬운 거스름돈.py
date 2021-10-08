MONEY = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, int(input())+1):
    cost = int(input())
    res = [0] * 8

    for i, x in enumerate(MONEY):
        if cost//x != 0 :
            res[i] = cost//x
            cost %= x

    print(f'#{tc}')
    print(*res)