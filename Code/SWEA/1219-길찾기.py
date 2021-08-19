for _ in range(10):
    T, N = map(int, input().split())
    lines = list(map(int, input().split()))
    graph = [[] for _ in range(100)]
    visit = [0] * 100
    stack = [0]

    for i in range(0, N*2, 2):
        graph[lines[i]].append(lines[i+1])
    
    while stack:
        x = stack.pop()
        visit[x] = 1
        for nx in graph[x]:
            if not visit[nx]:
                stack.append(nx)

    print(f'#{T}', visit[99])