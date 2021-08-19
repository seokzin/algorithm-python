for tc in range(1, int(input())+1):
    print(f'#{tc}')
    
    for i in range(int(input())):
        row = [1]
        for j in range(1, i+1):
            row.append(int(row[-1]*((i-j+1)/j)))

        print(*row)

# 조합 식을 응용해 풀었습니다.