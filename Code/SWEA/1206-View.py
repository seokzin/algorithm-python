for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    res = 0

    for i in range(2, n):
        # 좌우 2개의 합 중 최대값을 빼서 조망권 구한다. 
        # 기준보다 최대값이 크다면 조망권 수가 음수가 나오니 0으로 보정시켜준다. 
        res += max(arr[i] - max(arr[i-2:i]+arr[i+1:i+3]), 0)

    print(f'#{tc} {res}')