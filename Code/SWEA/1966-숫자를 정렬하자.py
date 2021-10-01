def selection_sort(s):
    if s:
        x = min(s)
        s.remove(x)
        return [x] + selection_sort(s)
    else:
        return []


for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))

    print(f'#{tc}', *selection_sort(arr))

# 재귀적 선택정렬 직접 구현해봄