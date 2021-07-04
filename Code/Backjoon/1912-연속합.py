n = int(input())
a = list(map(int, input().split()))

max_local = a[0]
max_global = a[0]

for i in range(1, len(a)):
  max_local = max(max_local + a[i], a[i])

  if max_local > max_global:
    max_global = max_local;


print(max_global)

# 카데인 알고리즘 (정리)