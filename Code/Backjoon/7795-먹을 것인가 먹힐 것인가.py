def binary_search(data, target):
  start, end = 0, len(data)-1

  while start <= end:
    mid = (start+end) // 2

    if data[mid] < target:
      start = mid+1
    else:
      end = mid-1

  return start

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  arr_a = sorted(list(map(int, input().split())))
  arr_b = sorted(list(map(int, input().split())))
  cnt = 0

  for a in arr_a:
    cnt += (binary_search(arr_b, a))  # a보다 작은 b의 개수들 리턴

  print(cnt)

# 중복 배열에서 가장 앞/뒤 위치 이분 탐색하는 방법 - https://yu5501.tistory.com/80