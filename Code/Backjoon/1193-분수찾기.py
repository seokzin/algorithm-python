n = int(input())

pos = 1 # 현재 position
lv = 1 # 층수 = 공차(d)

if n == 1:
  print('1/1')
else:
  while n > pos:
    lv += 1
    pos += lv

  if lv % 2 == 0:
    deno = pos - n + 1 # 분모
    nume = lv + 1 - deno # 분자 + 분모 = lv + 1 관계
  else:
    nume = pos - n + 1
    deno = lv + 1 - nume
  
  print( nume, '/', deno, sep="")

# 아무리 봐도 코드가 별로다. 풀이를 비교해서 개선하자...