T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = input()
    cnt = [0]*10

    for card in cards:
        cnt[int(card)] += 1

    for i in range(9, -1, -1):
        if cnt[i] == max(cnt):
            print(f'#{tc} {i} {cnt[i]}')
            break