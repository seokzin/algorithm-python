# Parametric Search - 최적화 문제를 결정 문제 (Y/N)로 바꿔 해결하는 기법. 이진 탐색을 이용하여 해결할 수 있다.
# 길이가 불규칙한 떡을 잘라 손님에게 M 만큼 줄 수 있는 절단기 높이 최댓값 구하기.

n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진탐색 시작
result = 0
while(start <= end):
  total = 0
  mid = (start + end) // 2
  for x in array:
    if x > mid:
      total += x - mid # 자른 떡 계산
  if total < m:
    end = mid - 1
  else:
    result = mid # 여기서 값을 기록
    start = mid + 1

print(result)
  