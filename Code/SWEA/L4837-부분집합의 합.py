def subset(x):
    global cnt

    if x == 12:  # 끝까지 탐색함
        if sum(bit) == N:  # 부분집합 개수가 N개라면
            sub_sum = 0

            for i in range(12):
                if bit[i]:
                    sub_sum += i+1  # 인덱스 보정

            if sub_sum == K:
                cnt += 1
    else:
        bit[x] = 0
        subset(x+1)

        bit[x] = 1
        subset(x+1)


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    bit = [0] * 12  # 부분집합에 해당 원소의 존재 상태 나타냄 (1, 0)
    cnt = 0

    subset(0)

    print(f"#{tc} {cnt}")

# 백트래킹