n = int(input())

arr = []

for i in range(n):
    arr.append(list(map(int, input().split()))) # list에 int 요소 가진 list 넣기

arr.sort(key=lambda x: (x[0], x[1]))

for i in arr:
    print(i[0], i[1])

# 람다로 정렬하는 법 https://dailyheumsi.tistory.com/67
# int() 요소 - string, obj, number. not tuple!