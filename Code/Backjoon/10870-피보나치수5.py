n = int(input())

a, b = 0, 1

for i in range(0, n):
  a, b = b, a+b

print(a)

# DP, 재귀는 써봤으니까 구조 분해 할당으로 풀어보고 싶었다. 이걸 구조분해할당으로 봐도 되나? 단순 쉼표이긴한데..