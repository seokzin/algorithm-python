import math
import sys
input = sys.stdin.readline

def compare(a, b, c, d):
  if a/b > c/d:
    return a, b, c, d
  else:
    return c, d, a, b

n, a, b, c, d = map(int, input().split())
a, b, c, d = compare(a, b, c, d)  # 가성비로 정렬

res = sys.maxsize

# 비싼 집을 1개씩 늘려가며 최소값 비교
for i in range(a):
  remain = max(n - i*c, 0)  # 채워야할 나머지 꽃 개수. 음수가 나오면 0 취급

  res = min(res, i*d + math.ceil(remain/a)*b)

print(res)

# 무지성으로 한 스텝씩 밟으면 되는데 예외처리가 디테일한 문제..