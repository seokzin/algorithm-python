n = int(input())
arr = list(map(int, input().split()))
ans = []
l, r = 0, n-1

while l < r:
  v = arr[l] + arr[r]

  if abs(mix) < ans[0]:
    ans[0] = abs(mix)
    ans[1] = (liq[l],liq[r])
  if mix > 0:
    r-=1
  elif mix < 0:
    l += 1
  else:
    return ans[1]
return ans[1]

print(*ans)