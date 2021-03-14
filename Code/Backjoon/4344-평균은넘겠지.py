n = int(input())

for _ in range(n):
  case = list(map(int, input().split()))
  cnt = 0

  avg = sum(case[1:])/case[0]

  for i in range(1, len(case)):
    if case[i] > avg: # i > 평균
      cnt += 1 

  print('%.3f' % (100 * cnt/case[0]), '%', sep='')

# 11) 소수점 3자리라는 출력 포맷 때문에 골탕 먹은 문제.
# 8) 중복되는 연산값은 if문 안에 넣으면 안된다. 따로 변수로 선언했을 때 176ms -> 72ms 성능 단축