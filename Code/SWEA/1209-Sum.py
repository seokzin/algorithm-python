def col_sum(i):  # 세로합
    col_sum = 0
    
    for j in range(100):
        col_sum += arr[j][i]

    return col_sum


def diag_sum():  # 대각합
    left_sum = 0
    right_sum = 0
    
    for i in range(100):
        left_sum += arr[i][i]
        right_sum += arr[99-i][i]

    return left_sum, right_sum


for tc in range(1, 11):
    arr = []
    T = int(input())

    for _ in range(100):
        row = list(map(int, input().split()))
        arr.append(row)

    pre_sum = []  # 부분합 리스트

    # 부분합 모두 구하기
    for i in range(100):
        # 1. 가로 합
        pre_sum.append(sum(arr[i]))

        # 2. 세로 합
        pre_sum.append(col_sum(i))

        # 3. 대각 합 - 튜플을 담으니 extend            
        pre_sum.extend(diag_sum())

    print(f'#{tc} {max(pre_sum)}')
