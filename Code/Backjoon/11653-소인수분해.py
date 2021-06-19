n = int(input())

while n > 1:
  for i in range(2, n+1):
    if n%i == 0:
      n //= i
      print(i)
      break

# n+1 자리에 sqrt를 도입하면 안되는 이유 -> n이 소수가 됐을 때..