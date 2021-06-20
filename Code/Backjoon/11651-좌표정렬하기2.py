import sys
input = sys.stdin.readline

n = int(input())
s = []

for _ in range(n):
  s.append(list(map(int, input().split())))

s.sort(key=lambda x: (x[1], x[0]))

for i in s:
  print(*i) # i[0], i[1]을 대신한다.

# 당연히 람다를 생각했다. 근데 이 문제는 특이하게 x 값을 정렬해서 입력하나보다. (조건엔 안적혀있음).. 그래서 y 정렬만 해줘도 되는데 정석대로 풀자!
# 2차원 리스트에 스타리스크를 적용할 수 있다.