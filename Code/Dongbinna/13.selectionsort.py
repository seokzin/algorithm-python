# 선택정렬 (selectionsort)
# 기준값과 뒷 값 중의 최소값을 스와핑. 다음 인덱스에 대해 반복

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[min_index] > array [j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]

print(array)