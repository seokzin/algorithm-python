for tc in range(1, 11):
    dump = int(input())

    box = sorted(list(map(int, input().split())))

    for _ in range(dump):
        box[0] += 1
        box[-1] -= 1
        box.sort()

    print(f'#{tc} {box[-1]-box[0]}')

# 단순무식한 풀이라고 생각합니다..