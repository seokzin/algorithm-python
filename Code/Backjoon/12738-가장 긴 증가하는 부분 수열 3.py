n = int(input())
arr = list(map(int, input().split()))
dp = []

for x in arr:
    start = 0
    end = len(dp)-1

    while start <= end:
        mid = (start+end) // 2

        if dp[mid] < x:
            start = mid+1
        else:
            end = mid-1

    if start >= len(dp):
        dp.append(x)
    else:
        dp[start] = x  # 아니라면 x보다 큰 값중 최소값과 대치

print(len(dp))

# LIS 2와 다른 점은 x의 범위. dp를 0으로 초기화하면 이 문제에선 틀린다. 
# 그래서 start 인덱스로 최대 판단함. 또는 dp[0]을 -10억+1 로 초기화