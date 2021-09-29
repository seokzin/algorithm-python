NUM = ('0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011')


def password(arr):  # 암호 추출    
    for row in arr:
        for idx, x in enumerate(row):
            if x == '1':
                pwd = row[idx:]
                pwd = pwd.rstrip('0')  # 뒤에 0제거
                pwd = pwd.zfill(56)  # 앞에 0 채워 56칸으로 보정
                
                return pwd


def decoding(s):  # 7비트씩 숫자로 변환
    temp = []

    for i in range(0, 56, 7):
        temp.append(NUM.index(s[i : i+7]))

    return temp


for tc in range(1, int(input())+1) :
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    pwd = password(arr)
    p = decoding(pwd)
    res = 0

    if (((p[0]+p[2]+p[4]+p[6])*3 + p[1]+p[3]+p[5]+p[7]) % 10 == 0):
        res = sum(map(int, p))
    
    print(f'#{tc}', res)