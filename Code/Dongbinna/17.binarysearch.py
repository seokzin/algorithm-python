# 이진 탐색 (정렬된 배열에 사용)
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  if array[mid] == target:
    return mid
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  else: # mid < target
    return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
  print('원소가 존재하지 않습니다.')
else:
  print(result + 1)

# bisect 라이브러리 - bisect_left(arr, x), bisect_right(arr, x) - 정렬된 arr에 x가 삽입될 좌or우 인덱스 반환. 이를 통해 특정 범위에 속하는 값 개수 구하기 응용