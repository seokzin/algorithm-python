# 정렬된 배열에서 특정 수의 개수 구하기
# 선형 탐색이 시간 초과 판정을 받을 수 있다.

# 7 2 / 1 1 2 2 2 2 3 / 4
from bisect import bisect_left, bisect_right

# 단일 값 뿐만 아니라 값이 [l_val, r_val]인 데이터의 개수를 반환하는 것도 가능
def count_by_range(array, left_value, right_value):
  right_index = bisect_right(array, right_value)
  left_index = bisect_left(array, left_value)
  return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
  print(-1)
else :
  print(count)