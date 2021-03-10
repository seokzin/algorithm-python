import sys
input = sys.stdin.readline # 이 방법도 좋지만 \n을 rstrip으로 항상 신경 써야하는 단점

n, m = map(int, input().split())

dic_num = {} # idx: name 쌍
dic_name = {} # name: idx 쌍

for i in range(1, n+1):
  s = input().rstrip() # \n 삭제
  dic_num[i] = s 
  dic_name[s] = i

for i in range(m):
  q = input().rstrip() 

  if q.isalpha():
    print(dic_name[q])
  else: # q.isdigit()
    print(dic_num[int(q)])

# Value로 Key 출력 방법 - 1. dict를 뒤집어 Value-Key dic을 만든다. 2. for문을 활용한다. 

# 실패1 (시간초과): for key, value in dic을 매번 사용해서 시간 초과인듯. 1번 방법으로 해결