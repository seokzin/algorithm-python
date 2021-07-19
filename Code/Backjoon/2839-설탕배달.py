n = int(input())
bag = 0

while n > 0:
  if n % 5 == 0:
    bag += n//5
    break

  n -= 3
  bag += 1 # 5kg로 나눠 떨어질 때 까지 3kg 봉지를 하나씩 채운다.

  if n < 0:
    bag = -1 # 딱 떨어지지 않는다면 -1 출력

print(bag)

# 설탕이 5의 배수가 될때까지 3을 먼저! 빼주는 것이 아이디어