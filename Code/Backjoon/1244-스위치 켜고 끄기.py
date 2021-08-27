n = int(input())

arr = [None] + list(map(int, input().split()))  # 인덱스 맞춤용

for _ in range(int(input())):
    gen, num = map(int, input().split())

    if gen == 1:
        for i in range(1, n//num+1):
            arr[i*num] = (arr[i*num]+1) % 2  # NOT 연산
    else:
        j = 0
        
        while num-j > 0 and num+j <= n and arr[num-j] == arr[num+j]:
            arr[num-j] = arr[num+j] = (arr[num+j]+1) % 2  # NOT 연산
            j += 1

for i in range(len(arr)//20 + 1):
    print(*arr[20*i+1 : 20*(i+1)+1])

# 사소한 규칙들이 까탈스러운 문제였습니다.