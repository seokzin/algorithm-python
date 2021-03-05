n = int(input())
n_list = list(input().split())

m = int(input())
m_list = list(input().split())

n_list.sort() # 이진탐색의 선행 조건

def bs(arr, val, low, high):
  if low > high:
      return False
  
  mid = (low + high) // 2

  if arr[mid] > val:
      return bs(arr, val, low, mid - 1)
  elif arr[mid] < val:
      return bs(arr, val, mid + 1, high)
  else:
      return True

for i in m_list:
    if bs(n_list, i, 0, n-1):
        print(1)
    else:
        print(0)

# 1. if m_set in n_set 단순 비교: 시간 초과
# 2. 교집합 추려낸 후 if m_set in inter_set 비교: 시간 초과
# 시간 복잡도를 고려해야 한다.

# sort와 sorted의 차이?