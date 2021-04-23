n = int(input()) # target

pos = 1 # 현재 position
d = 6 # 공차
res = 1

if n == 1:
  pass
else:
  while n > pos:
    pos += d
    d += 6
    res += 1

print(res)

# pass continue 차이 살짝 정리
# 은근히 까탈스럽게 풀었네.. 다른 풀이랑 비교해보기