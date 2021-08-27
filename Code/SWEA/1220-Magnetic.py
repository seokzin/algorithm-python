import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    arr = list(zip(*data))  # Transpose
    cnt = 0
    
    for row in arr:
        flag = 0

        for i in range(N):
            if row[i] == 1 and not flag:
                flag = 1
            elif row[i] == 2 and flag:
                cnt += 1
                flag = 0
        
    print(f'#{tc}', cnt)