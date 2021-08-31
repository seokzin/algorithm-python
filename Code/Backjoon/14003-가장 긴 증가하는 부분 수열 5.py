n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n  # 최대 길이 담을 테이블
lis = []  # LIS 담을 리스트

for i in range(n):
    start = 0
    end = len(lis)-1

    while start <= end:
        mid = (start+end) // 2

        if lis[mid] < arr[i]:
            start = mid+1
        else:
            end = mid-1

    if start >= len(lis):
        lis.append(arr[i])
        dp[i] = len(lis)
    else:
        lis[start] = arr[i]  # 아니라면 x보다 큰 값중 최소값과 대치
        dp[i] = start+1  # 현위치+1 저장

res = []
idx = max(dp)

for i in range(n-1, -1, -1):
    if dp[i] == idx:
        res.append(arr[i])
        idx -= 1

print(max(dp))
print(*res[::-1])