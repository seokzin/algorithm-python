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
    v, e = map(int, input().split())
    graph = []
    parent = list(range(v+1))
    res = 0

    for _ in range(e):
        a, b, c = map(int, input().split())
        graph.append((c, a, b))

    graph.sort()

    for w, s, e in graph:
        if find(s) != find(e):
            union(s, e)
            res += w

    print(f"#{tc}", res)
