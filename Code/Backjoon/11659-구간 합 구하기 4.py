import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0] * (n+1) # 부분합, 인덱스 보정

sum_arr[1] = arr[0] # n=1일 때 할당

for i in range(1, n):
  sum_arr[i+1] = sum_arr[i] + arr[i]

for _ in range(m):
  i, j = map(int, input().split())
  if i == 1:
    print(sum_arr[j])
  else:
    print(sum_arr[j] - sum_arr[i-1])

# sys.readline 안쓰면 틀린다.