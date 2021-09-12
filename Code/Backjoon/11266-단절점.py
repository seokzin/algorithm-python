import sys
sys.setrecursionlimit(10**4)

input = sys.stdin.readline


def dfs(x, isroot):
    global cnt
	
    cnt += 1
    visit[x] = cnt

    now = visit[x]
    child = 0
	
    for nx in graph[x]:  # 인접 노드
        if not visit[nx]:
            child += 1

            min_nx = dfs(nx, 0)  # 자식 중 최소 번호

            if not isroot and min_nx >= visit[x]:  # 최소 번호가 현 노드보다 크다면 단절점
                res.append(x)
			
            now = min(now, min_nx)  # 최소 번호 저장
        
        else:
            now = min(now, visit[nx])

    if isroot and child > 1:  # 루트 노드며 자식이 2개 이상이면 단절점
        res.append(x)
    
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

res = sorted(list(set(res)))

print(len(res))
print(*res)

# 알고리즘에 대한 이해 부족
# 단절점을 리스트로 담을 때 중복 처리가 별로