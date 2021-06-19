m = int(input())
n = int(input())
res = [] # 소수 담을 리스트

for i in range(m, n+1):
  if i == 1:
    pass # 1을 예외처리 안해도 range(2, 1)에서 무시되지만 에라토스테네스를 확실히 구현하기 위해
  elif i == 2:
    res.append(i)
  else:
    for j in range(2, i):
      if i%j == 0:
        break
      elif j == i-1:
        res.append(i)

if not res: # 소수가 없을 때
  print(-1)
else:
  print(sum(res))
  print(min(res))

# 루트 i까지 하면 더 효율적이지 않을까? 막상 하려니 14)라인 때문에 복잡해진다. 필요하면 그때 하자
# 14) 처럼 for문이 무사히 끝났을 때 연산하고싶으면 어떤 방법을 써야할까..? - 함수의 리턴으로 할 수도 있다.