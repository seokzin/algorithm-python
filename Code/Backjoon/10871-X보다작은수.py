n, x = map(int, input().split(' '))

arr = list(map(int, input().split(' ')))

for i in arr:
  if i < x:
    print(i, end=' ')
  # if arr[i] >= x:
  #   arr.remove(arr[i])

# for문을 통해 remove, del시 원본이 수정되어 반복 순서가 점프된다. https://devpouch.tistory.com/110