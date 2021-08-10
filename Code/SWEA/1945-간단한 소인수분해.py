T = int(input())

div = (2, 3, 5, 7, 11)

for tc in range(1, T+1):
    n = int(input())

    res = [0]*5  # a b c d e 카운트

    for i in range(5):
        while n % div[i] == 0:
            n //= div[i]
            res[i] += 1

    print(f'#{tc}', end=' ')
    print(*res)