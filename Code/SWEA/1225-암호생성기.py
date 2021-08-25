for _ in range(1, 11):
    tc = int(input())
    arr = list(map(int,input().split()))
    cnt = 1  # 감소 카운트

    while True:
        arr[0] -= cnt
        cnt = cnt%5 + 1
        arr.append(arr.pop(0))
        
        if arr[-1] <= 0:
            arr[-1] = 0
            break

    print(f'#{tc}', *arr)
