n = int(input())
num = 666 # 666으로 초기화
cnt = 0

while True:
  if '666' in str(num):
    cnt += 1

  if cnt == n:
    print(num)
    break

  num += 1

# 수열의 규칙성을 찾기가 너무 어려우니 단순무식하게 훑기
# 다른 방법으로 풀어볼까 했는데 일부러 복잡해지는 느낌이다. 그냥 while-break