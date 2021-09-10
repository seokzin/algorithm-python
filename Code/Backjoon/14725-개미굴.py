n = int(input())
arr = [['']] + sorted(list(input().split())[1:] for _ in range(n))  # 더미
cnt = 0

for i in range(1, n+1):
    for j in range(len(arr[i])):
        if len(arr[i-1]) <= j or arr[i-1][j] != arr[i][j]:
            break
        else:
            count = j

    for j in range(cnt+1, len(arr[i])):
        print("--" * j + arr[i][j])

# 전에 것과 틀리는 순간 반복 탈출 후 모두 출력하는 것이 핵심인듯