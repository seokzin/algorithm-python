import math

t = int(input())

for _ in range(t):
  x, y = map(int, input().split())
  dis = y - x # 시작점을 0으로 동기화 = 거리에만 집중
  cnt = 0

  root = int(math.sqrt(dis)) # 작명이 참 난감하다. 루트의 버림값

  if dis == root**2:
    cnt = root*2 - 1
  elif dis <= root**2 + root:
    cnt = root*2
  else: # dis < (root+1)**2
    cnt = root*2 + 1

  print(cnt)

# DP도 아닌 것 같을 때 -> 직접 구해보며 규칙성을 찾는게 답이다..
# 정수의 범위가 2^32 -> 제곱수의 힌트로 볼 수 있다. 실제 제곱수마다 걸음의 피라미드가 완성된다.
# 또 루트 올림 값마다 뒤에서 카운트가 오른다.
# 제곱수가 핵심 키다..!
# 풀고 굉장히 뿌듯했다..! 제곱수가 2.XXX인 4~9까지 예시를 구해서 조건문이 3파트인걸 증명
# 특히 1, 2 일때 예외처리 없이 한번에 된다느게 굉장히 맘에드는 코드다.