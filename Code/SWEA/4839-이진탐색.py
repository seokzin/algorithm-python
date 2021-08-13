def binary_search(x):
    start = 1
    end = p
    cnt = 0

    while start <= end:
        mid = (start+end) // 2

        if x == mid:
            return cnt
        elif x > mid:
            start = mid
            cnt += 1
        else: 
            end = mid
            cnt += 1


T = int(input())

for tc in range(1, T+1):
    p, a, b = map(int, input().split())

    score = binary_search(b) - binary_search(a)
    res = 0

    if score > 0:
        res = 'A'
    elif score < 0:
        res = 'B'
    else:
        res = '0'

    print(f"#{tc} {res}")
