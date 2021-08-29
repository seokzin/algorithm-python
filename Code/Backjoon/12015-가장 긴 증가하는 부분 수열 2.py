n = int(input())
arr = list(map(int, input().split()))
dp = [0]

for x in arr:
    start = 0
    end = len(dp)-1

    if dp[-1] < x:  # x가 가장 큰 값이면 dp에 추가
        dp.append(x)
    else:

        while start <= end:
            mid = (start+end) // 2

            if dp[mid] < x:
                start = mid+1
            else:
                end = mid-1

        dp[start] = x  # 아니라면 x보다 큰 값중 최소값과 대치

print(len(dp) - 1)

# 2중 for문은 시간초과 - 이진탐색을 해야함
# 코드는 이해했으나 응용을 위해 다시 훑어보기