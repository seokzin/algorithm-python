n = int(input())
arr = list(map(int, input().split()))

l, r = 0, n-1
ans = [abs(arr[l]+arr[r]), (arr[l],arr[r])]

while l < r:
  mix = arr[l] + arr[r]

  if abs(mix) < ans[0]:
    ans[0] = abs(mix)
    ans[1] = (arr[l], arr[r])

  if mix > 0:
    r -= 1
  elif mix < 0:
    l += 1
  else:
    break

print(*ans[1])

# 다시 살펴보기
# 2473 세 용액 묶어서 풀기