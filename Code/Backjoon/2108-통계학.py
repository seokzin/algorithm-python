import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
a = [] # N개의 수 담을 리스트

for _ in range(n):
  num = int(input())
  a.append(num)


# 1. 산술평균
def mean():
  return round(sum(a)/n)

# 2. 중앙값
def med():
  return sorted(a)[(n-1)//2] 

# 3. 최빈값
def mode():
  a_mode = Counter(sorted(a)).most_common() # 2번째 작은 값 쉽게 얻기 위해 선정렬

  if n > 1:
    if a_mode[0][1] == a_mode[1][1]: # 최빈값이 2개 이상일 때 2번째 작은값 리턴
      return a_mode[1][0]
  
  return a_mode[0][0] # 나머지 케이스 (return이 함수 종료시키니 else를 묶을 수 있었다.)

# 4. 범위
def scope():
  return max(a) - min(a)

print(mean())
print(med())
print(mode())
print(scope())

# '//' 연산은 버림이다! 산술 평균은 반올림 round 값이어야 한다!
# 4개의 문제를 합친 것이다. 스스로 수십 가지 케이스를 만드는 훈련을 해야한다.