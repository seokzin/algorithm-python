NUM = ('0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011')


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

        bin_pwd = bin_pwd.strip('0')  # 앞뒤에 0 제거
        bin_pwd = bin_pwd.zfill(56 * round(len(bin_pwd) / 56))  # 가까운 56 배수로 0 개수 보정
        temp.append(bin_pwd)
    
    return temp


def decoding(pwds):  # 7비트씩 숫자로 변환
    temp = []

    for pwd in pwds:
        dec = []

        for i in range(0, 56, 7):
            dec.append(NUM.index(pwd[i : i+7]))

        temp.append(dec)

    return temp


for tc in range(1, int(input())+1) :
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    pwds = hex_to_bin(password(arr))
    p_list = decoding(pwds)
    res = 0

    for p in p_list:
        if (((p[0]+p[2]+p[4]+p[6])*3 + p[1]+p[3]+p[5]+p[7]) % 10 == 0):
            res = sum(map(int, p))
    
    print(f'#{tc}', res)