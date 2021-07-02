import sys
INF = sys.maxsize

n = int(input())
arr = sorted(list(map(int, input().split()))) # 먼저 정렬!
ans = [INF, ()] # (농도, 용액 종류)

for i in range(n-2):
  l = i+1
  r = n-1

  while l < r:
    mix = arr[i] + arr[l] + arr[r]

    if abs(mix) < ans[0]:
      ans[0] = abs(mix)
      ans[1] = (arr[i], arr[l], arr[r])

    if mix > 0:
      r -= 1
    elif mix < 0:
      l += 1
    else:
      break

print(*ans[1])

# 투포인터에 대해.. 정렬 필요 이유
# PyPy로 맞는 문제 --;