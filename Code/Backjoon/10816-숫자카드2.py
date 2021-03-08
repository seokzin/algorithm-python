from bisect import bisect_left, bisect_right

n = int(input())
n_list = list(input().split())

m = int(input())
m_list = list(input().split())

n_list.sort()

def bs_cnt(arr, l, r):
  r_idx = bisect_right(arr, r)
  l_idx = bisect_left(arr, l)
  return r_idx - l_idx

for i in m_list:
  print(bs_cnt(n_list, i, i), end=' ')

# 시도 1. count - 당연히 시간 초과. - 
# 시도 2. bisect 라이브러리 사용 - 라이브러리에 의존이 좋은 방법은 아닌듯.. 당연히 이진탐색 기반의 라이브러리라 성공은 하는 것 같은데