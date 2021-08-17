T = int(input())

for tc in range(1, T+1):
    datas = input().replace('()', 'V')
    cnt = 0
    res = 0

    for data in datas:
        if data == '(': 
            cnt += 1
        elif data == 'V':  # Laser
            res += cnt
        elif data == ')':
            cnt -= 1
            res += 1

    print(f'#{tc} {res}')

# replace - 괄호와 레이저 구분을 위한 예외처리를 없애기 위해