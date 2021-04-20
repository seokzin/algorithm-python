while True:
  a = list(map(int, input().split()))
  max_a = max(a)

  if sum(a) == 0:
    break
  
  a.remove(max_a)
  if a[0]**2 + a[1]**2 == max_a**2:
    print('right')
  else:
    print('wrong')

# 이게 최선이였을까? 최대값을 pop하는 방법은 무엇?
# a[0] + a[1] = 0 대신 sum(a)를 쓰는게 메모리적으로 바람직한가