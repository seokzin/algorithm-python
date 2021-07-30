import math
import sys
input = sys.stdin.readline

def compare(a, b, c, d):
  if a/b > c/d:
    return a, b, c, d
  else:
    return c, d, a, b

n, a, b, c, d = map(int, input().split())

an, bn, cn, dn = compare(a, b, c, d)

compare_min = sys.maxsize

for flower1 in range(an):
  flower2 = math.ceil((n - flower1 * cn)/an)
  price1 = flower1 * dn 
  price2 = flower2 * bn

  if price2 < 0: 
    price2 = 0
  
  compare_min = min(compare_min, price1+price2)

print(compare_min)