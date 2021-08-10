T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_sum = []

    for i in range(N+1-M):
        arr_sum.append(sum(arr[i:i+M]))

    print(f'#{tc} {max(arr_sum)-min(arr_sum)}')