T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))
    now = 0  # 현 위치 인덱스
    cnt = 0  # 충전 횟수

    while now < N-K:
        for n in range(now+K, now, -1):
            if n in charges:
                cnt += 1
                now = n
                break
        else:  # for문을 완료했다 = 다음 정류장을 찾지 못했다
            cnt = 0
            break

    print(f'#{tc} {cnt}')