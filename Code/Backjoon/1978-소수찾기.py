n = int(input())

arr = list(map(int,input().split()))

prime = 0 # 소수 개수

for i in arr:
  cnt = 0

  if i < 2:
    continue
  elif i == 2:
    prime += 1
    continue
  else: # i > 2
    for j in range(2, i):
      if i % j == 0: # 소수가 아님
        cnt += 1
  
  if cnt == 0:
    prime += 1

print(prime)

# 12) i = 2 일 때 prime이 2번씩 체크됨 - continue로 해결
# 다른 풀이 - break를 활용해 cnt 변수 역할을 대신 해보기