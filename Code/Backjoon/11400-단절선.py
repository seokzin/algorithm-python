import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def dfs(x, parent):
    global cnt
	
    cnt += 1
    visit[x] = cnt

    now = visit[x]
	
    for nx in graph[x]:  # 인접 노드
        if nx == parent:  # 부모일시 패스
            continue

        if not visit[nx]:
            min_nx = dfs(nx, x)  # 자식 중 최소 번호

            if min_nx > visit[x]:
                res.append(sorted((x, nx)))
        
            now = min(now, min_nx)  # 최소 번호 저장
    
        else:
            now = min(now, visit[nx])

    return now


v, e = map(int, input().split())

graph = [[] for _ in range(v+1)]
visit = [0 for _ in range(v+1)]
res = [] # 단절점 리스트
cnt = 0 # 노드 번호

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1, v+1):
    if not visit[i]:
        dfs(i, 1)

print(len(res))
for row in sorted(res):
    print(*row)

# 알고리즘에 대한 이해 부족