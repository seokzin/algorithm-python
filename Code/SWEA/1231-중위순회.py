def inorder(n):
    if n <= N:
        inorder(n*2)  # left
        res.append(arr[n])  # root
        inorder(n*2+1)  # right


for tc in range(1, 11):
    N = int(input())
    arr = ['']
    res = []

    for i in range(N):
        data = input().split()
        arr += data[1]

    inorder(1)

    print(f'#{tc} ',*res, sep='')