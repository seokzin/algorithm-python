# m, n = map(int, input().split())

# for i in range(m, n+1):
#   if i == 1:
#     pass
#   elif i == 2 or i == 3:
#     print(i)
#   else:
#     root = int(i**0.5)
    
#     for j in range(2, root+1):
#       if i%j == 0:
#         break
#       elif j == root:
#         print(i)

m, n = map(int, input().split())

def isPrime(i):
  if i == 1:
    return False
  elif i == 2 or i == 3:
    return True
  else:
    root = int(i**0.5)
    
    for j in range(2, root+1):
      if i%j == 0:
        return False
    return True


for i in range(m, n+1):
  if isPrime(i):
    print(i)

# starisk 문법 정확히 정리하자.
# 갑자기 헷갈린건데 map(int, input())은 어떨때 쓰이더라?
# sqrt 대신 **(0.5)가 있었다..
# 100만이 넘어가면 복잡도 암산을 어떻게 할까. 의도는 에라토스테네스이긴한데
# for문 안에 연산을 넣지 말자!!! root를 빼니까 5476 -> 1052ms로 줄였다.
# 왜 함수화 한건 시간초과 안뜨고 for문은 시간초과 뜨지?? - 파이썬 함수 효율이 좋나?
# starisk 문법 정확히 정리하자.
# 갑자기 헷갈린건데 map(int, input())은 어떨때 쓰이더라?
# sqrt 대신 **(0.5)가 있었다..
# 100만이 넘어가면 복잡도 암산을 어떻게 할까. 의도는 에라토스테네스이긴한데
# 시간초과 뜨는 이유 - for 연산마다 sqrt 연산을 해서?? PyPy는 맞았따.
# res 리스트를 두지 않고 바로 print를 했다. 출력에서 O(n)을 할애하는 것이 비효율 적이라 생각 -> 역시나 시간초과
# 에라토스테네스의 체 실패 -> 매번 100만개의 소수 구하는 것이 비효율적이었나보다.