import sys

n = int(input())

zero = [1, 0, 1] # fibo(0) 호출 횟수 arr
one = [0, 1, 1] # fibo(1) 호출 횟수 arr

for i in range(3, 41):
  zero.append(zero[i-1] + zero[i-2])
  one.append(one[i-1] + one[i-2])

for _ in range(n):
  q = int(input())

  print(zero[q], one[q])

# 초보때는 코드가 간결한 것 보다 쉬운게 낫다.