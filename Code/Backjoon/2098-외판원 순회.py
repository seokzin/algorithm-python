import sys

input = sys.stdin.readline

INF = sys.maxsize

n = int(input())
city = []  # city[a][b] = a도시에서 b도시 가는 비용
for _ in range(n):
    city.append(list(map(int, input().split())))

dp = [[INF] * (1<<n) for _ in range(n)]  # DP[now][bitmask_path]

def move(now, path):
    if path == (1<<n)-1:  # 모두 방문했을 때
        return INF if city[now][0] == 0 else city[now][0]  # 0으로 가는 방법 없다면 INF 반환 

    if dp[now][path] != INF:  # 이미 계산되었다면 그 값을 반환
        return dp[now][path]  

    for i in range(1, n):
        if not path & (1<<i) and city[now][i] != 0:
            dp[now][path]= min(dp[now][path], move(i ,path | (1<<i)) + city[now][i])
    return dp[now][path]

print(move(0,1))

# 비트 마스크 -> 각 비트 자리수가 방문한 곳을 표시
# DFS가 아닌가?
# 비트 마스크 개념은 너무 생소하다.. 잠시 맛만 보고 나중에 다시 오겠다