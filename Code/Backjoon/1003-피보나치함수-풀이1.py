t = int(input())

zero = [1, 0]
one = [0, 1]

for i in range(2, 41):
  zero.append(zero[i-1] + zero[i-2])
  one.append(one[i-1] + one[i-2])

for _ in range(t):
  n = int(input())
  print(zero[n], one[n])

# 여러 테스트 케이스를 요구하니 초기에 fibo 값을 미리 계산해두는 것이 좋아보인다.