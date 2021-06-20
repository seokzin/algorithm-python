prime = [True] * 10001
prime[0] = prime[1] = False

# 에라토스테네스의 체
for i in range(2, 101): # root(10000) 까지만 필터링
  if prime[i]:
    for j in range(i*2, 10001, i): # i 다음 값부터 필터링 한다.
      prime[j] = False

t = int(input())

for _ in range(t):
  n = int(input()) # n = 짝수

  for i in range(n//2, 1, -1): # 중앙부터 탐색을 확장해야 가장 작은 차를 출력할 수 있음
    if prime[i] == True and prime[n-i] == True:
      print(i, n-i)
      break

# 에라토스테네스로 한다음 for문으로 합 성사할때까지 찾기? find 써야하나?
# prime 리스트에 append와 단순히 F, T 변환의 효율이 어떠한 차이를 보일까?
# 숫자를 1씩 탐색하는 것이랑 True를 기반으로 2중 for문을 돌며 합이 n이 되는걸 체크하는 거랑 효율 차이는 어떨까?