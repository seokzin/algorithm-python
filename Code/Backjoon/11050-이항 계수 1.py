from math import factorial as f
n, k = map(int, input().split())

print(f(n) // (f(k) * f(n-k)))

# 쉬워서 숏코딩 연습..