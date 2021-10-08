def to_dec(n, ntype):
    tmp = 0

    for i, x in enumerate(list(map(int, n))[::-1]):
        tmp += x * (ntype**i)

    return tmp


def check(n, ntype):
    tmp = 0

    for x in bi:
        tmp = tmp*2 + int(x)

    for i in range(len(bi)):
        res.append(tmp ^ (1<<i))

    for i in range(len(tr)):
        a = 0
        b = 0

        for j in range(len(tr)):
            if i != j:
                a = a*3 + int(tr[j])
                b = b*3 + int(tr[j])
            else:
                a = a*3 + (int(tr[j])+1) % 3
                b = b*3 + (int(tr[j])+2) % 3

        if a in res:
            return a

        if b in res:
            return b


for tc in range(1, int(input())+1):
    bi = input()
    tr = input()

    res = []

    print(f'#{tc}', check(bi, 2))

# 어려웠음