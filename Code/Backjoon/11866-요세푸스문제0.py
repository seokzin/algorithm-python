n, k = map(int, input().split())

arr_a = list(range(1,n+1))
arr_k = [] # 사망자
idx = 0

while len(arr_a) > 0:
  idx = (idx + (k-1)) % n # 3 6 2 5
  n -= 1

  arr_k.append(arr_a[idx])
  arr_a.remove(arr_a[idx])

print("<" + ", ".join(list(map(str, arr_k))) + ">")

# len(arr) 대신 arr[-1]을 활용한다..
# 1. 반례) n이 1일 때. <1, > 으로 출력됐다.
# join() - 리스트 사이에 기호를 넣어 문자열로 표현. 성능 차이는 거의 X. (이를 통해 간단화, n=1 반례 해결!). 다만 join의 변수는 str이여야 한다. https://hyesun03.github.io/2017/04/08/python_int_join/