import math

r = int(input())

print('%.6f' %(math.pi * r * r)) # 유클리드 원넓이
print('%.6f' %(2 * r * r)) # 택시 원넓이 (마름모)

# 물론 6자리 안지켜도 정답이지만 정확한 출력을 위해 6자리까지 출력함