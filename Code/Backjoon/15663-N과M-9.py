n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))
visit = [0] * len(li) 
s = []
ans = []

def dfs():
  if len(s) == m:
    ans.append(tuple(s))
    return
  
  for i in range(n):
    if not visit[i]:
      s.append(li[i])
      visit[i] = 1
      dfs()
      s.pop()
      visit[i] = 0

dfs()

for i in sorted(list(set(ans))):
  print(*i)


# 베이스: N과M(1)
# 아이디어: 답을 모아 set으로 중복 제거 후 정렬 
# append(list) 하면 왜 빈 리스트가 추가될까? 왜 copy를 해야 정상 작동할까?
# unhashable type: 'list' - 해쉬 가능한(변형 불가능한) 문자열, 숫자, 튜플만 set에 넣을 수 있다.
# if li[i] not in s 사용시 [9, 9] 같은 케이스가 삭제 된다. visit 도입 해야함