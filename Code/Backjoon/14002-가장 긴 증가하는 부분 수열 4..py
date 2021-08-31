n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)   # 증가하지만 연속하지 않는 것들 걸러줌

res = []
idx = max(dp)

for i in range(n-1, -1, -1):
    if dp[i] == idx:
        res.append(arr[i])
        idx -= 1

print(max(dp))
print(*res[::-1])

# 반례) 3, 1, 2 (뒤에서부터 출력해야한다)
