for tc in range(1, int(input())+1):
    N = int(input())
    
    print(f'#{tc}')
    
    for i in range(N):
        row = [1]
        for j in range(1, i+1):
            row.append(int(row[-1]*((i-j+1)/j)))
        print(*row)
