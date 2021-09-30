NUM = {'112':0, '122':1, '221':2,'114':3, '231':4,'132':5, '411':6, '213':7, '312':8, '211':9}


def password(arr):  # 16진수 암호 추출
    temp = []

    for row in arr:
        for x in row:
            if x:
                pwds = row.split('0')
                for pwd in pwds:
                    if pwd and pwd not in temp:
                        temp.append(pwd)

    return temp


def hex_to_bin(pwds):
    temp = []

    for pwd in pwds:
        bin_pwd = ''

        for x in pwd:
            c = bin(int('0x'+x, 16))[2:].zfill(4)
            bin_pwd += c

        bin_pwd = bin_pwd.rstrip('0')  # 뒤에 0 제거
        temp.append(bin_pwd)
    
    return temp


def decoding(pwds):  # 7비트씩 숫자로 변환
    temp = []

    for pwd in pwds:
        dec = []
        a = b = c = 0  # bit checking

        for i in range(len(pwd)-1, -1, -1):
            if not b and not c and pwd[i] == '1':
                a += 1
            elif a and not c and pwd[i] == '0':
                b += 1
            elif a and b and pwd[i] == '1':
                c += 1
            elif c and pwd[i] == '0':
                mul = min(a, b, c)
                dec.append(NUM[str(a//mul)+str(b//mul)+str(c//mul)])
                a = b = c = 0
        
        temp.append(dec[::-1])  # 역탐색을 다시 뒤집어준다.
        
    return temp


for tc in range(1, int(input())+1) :
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    pwds = hex_to_bin(password(arr))
    p_list = decoding(pwds)
    res = 0

    for p in p_list:
        if (((p[0]+p[2]+p[4]+p[6])*3 + p[1]+p[3]+p[5]+p[7]) % 10 == 0):
            res += sum(map(int, p))
    
    print(f'#{tc}', res)