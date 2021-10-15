def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        x, y = y, x

    parent[y] = x


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    parent = list(range(n+1))

    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)

    res = [find(i) for i in range(n+1)]

    print(f'#{tc}', len(set(res))-1)