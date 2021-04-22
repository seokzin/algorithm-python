n = int(input())

result = 0
p = list(map(int, input().split()))

p.sort()

for i in range(n):
  result += sum(p[0 : i+1])

print(result)

# 4라인 - list 안붙이면 어떤 결과가 나오길래?