n = int(input())

arr = []

for i in range(n):
    arr.append(list(input().split()))

arr.sort(key=lambda x: int(x[0])) 

for i in range(n):
    print(arr[i][0], arr[i][1])

# 람다로 정렬하는 법 https://dailyheumsi.tistory.com/67