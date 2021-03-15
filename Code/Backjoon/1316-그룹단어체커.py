n = int(input())
res = 0

for _ in range(n):
  s = input()
  cnt = 0

  for i in range(len(s)-1):
    if s[i] != s[i+1]:
      if s[i] in s[i+1:]:
        cnt += 1
  
  if cnt == 0:
    res += 1

print(res)

# F = break, T = cnt++ 형태의 문제에서 실수가 잦다. 이럴 땐 cnt(전역)와 임시cnt(지역)을 두어 2중 장치를 취해보자.
# range(0)일 때 for문 - 아무 일도 일어나지 않음 (에러X)