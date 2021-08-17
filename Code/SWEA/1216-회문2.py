def palindrome(l):
    for i in range(100):
        for j in range(101-l):
            row = arr[i][j:j+l]
            col = arr_t[i][j:j+l]

            if row == row[::-1] or col == col[::-1]:
                return l

for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(100)]
    arr_t = list(zip(*arr))  # Transpose

    for l in range(100, 0, -1):  # 회문 길이 
        if palindrome(l):  # 역탐색이니 함수값이 출력되면 그게 곧 최대값
            print(f"#{N}", palindrome(l))
            break
