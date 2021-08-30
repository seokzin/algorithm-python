import math
PI = math.pi

x1,y1,r1, x2,y2,r2 = map(float, input().split())
(r1, r2) = (r1, r2) if r1 > r2 else (r2, r1)

d = ((x1-x2)**2 + (y1-y2)**2) ** 0.5

if d >= r1 + r2:
    ans = 0

if d <= (r1-r2):
    ans = PI * (r2**2)

if r1-r2 < d < r1+r2:
    x = (r1**2 - r2**2 + d**2) / (2*d)
    y = (r1**2 - x**2) ** 0.5
    theta1 = math.atan2(y, x)/PI * 180
    theta2 = math.atan2(y, d-x)/PI * 180
    ans = PI*r1**2 * theta1/180 + PI*r2**2 * theta2/180 - d*y

print('%.3f' % ans)