import sys
input = sys.stdin.readline

def dfs(idx, pre_sum):
    global cnt

    if idx >= n:
        return
        
    pre_sum += nums[idx]

    if pre_sum == s:
        cnt += 1

    dfs(idx+1, pre_sum-nums[idx])
    dfs(idx+1, pre_sum)

n, s = map(int, input().split())
cnt = 0

nums = list(map(int, input().split()))

dfs(0, 0)

print(cnt)

# 단순 무식한 풀이 -> 모든 경우의 수 탐색