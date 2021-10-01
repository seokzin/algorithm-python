for tc in range(1, int(input())+1):
    n, arr = map(int, input().split())
    bits = str(bin(arr))[2:][-n:]
    res = 'ON' if bits == '1'*n else 'OFF'
    
    print(f'#{tc}', res)