# 퀵 정렬 (quick sort)
# 기준(피봇)을 정해 대소를 나눈다.
# 코드 구조가 한 번에 이해되진 않아서 다른 자료를 많이 참고해 익숙해지자.
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: # 원소가 1개일 때 종료
    return
  pivot = start # 피벗은 첫 번째 원소
  left = start + 1
  right = end
  
  while(left <= right):
    # 피벗보다 큰 데이터 찾을 때까지 반복
    while(left <= end and array[left] <= array[pivot]):
      left += 1
    # 피벗보다 작은 데이터 찾을 때까지 반복
    while(right > start and array[right] >= array[pivot]):
      right -= 1
    if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: # 엇갈리지 않았다면 작은 데이터과 큰 데이터를 교체
      array[left], array[right] = array[right], array[left]

  # 분할 이후 나눈 부분별로 재귀 수행
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)