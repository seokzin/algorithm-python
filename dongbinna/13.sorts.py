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

# 삽입정렬 (insertion sort)
# 기준값과 다음 값을 비교해 어디에 넣을지 정한다.
for i in range(1, len(array)):
  for j in range(i, 0, -1): # i부터 1까지 감소 반복
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break # 자기보다 작은 데이터 만나면 그 위치에서 멈춤

print(array)