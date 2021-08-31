n = int(input())
arr = list(map(int, input().split()))

dp = [x for x in arr]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+arr[i])

print(max(dp))

# dp에 카운트가 아닌 합을 저장한다.