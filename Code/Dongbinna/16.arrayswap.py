# 두 배열의 원소 교체. A의 값을 최대로 만들기

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]
  else: # A의 원소가 B의 원소보다 크거나 같을 때 탈출
    break

print(sum(a))