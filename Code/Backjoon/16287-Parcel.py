import sys

w, n = map(int, input().split())
arr = list(map(int, input().split()))
visit = [0] * w

for i in range(n):
    for j in range(i+1, n):  # 검증 파트
        if arr[i]+arr[j] < w and visit[w-arr[i]-arr[j]]:
            print("YES")
            sys.exit()
    
    for j in range(i):  # 메모이제이션 파트
        if arr[i] + arr[j] < w:
            visit[arr[i] + arr[j]] = 1

print("NO")

# DP도 시간 초과다. - O(N*W)
# 2개씩 합을 묶어 투포인터? - O(N*N)
# 더 줄이면 탐색을 이분탐색이 있는데.. 얘는 정렬이 안돼있어서 X
# 로직 이해는 됐는데 코드 돌아가는 과정은 시뮬이 안됨. 다시 보자