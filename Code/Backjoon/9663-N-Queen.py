n = int(input())
s = [0] * (n+1)

res = 0

def pos(x): # 배치 가능성 검증
  for i in range(1, x):
    if s[x]==s[i] or abs(s[x]-s[i]) == x-i:
      return False
  return True

def dfs(idx):
    global res

    if idx > n:
      res += 1
    else:
      for i in range(1, n+1):
        s[idx] = i
        if pos(idx):
          dfs(idx+1)

dfs(1)

print(res)

# 배열 값 대체하는 것과 append pop 쓰는 것의 복잡도 차이? - 둘디 O(1)
# s.append()로 풀고싶었는데 도저히 내 방식대로 DFS를 못하겠다. 시뮬이 안된다.. 내공 부족
# 이 방식은 말을 빼는게 아닌 단순히 리스트 덮어쓰기라 추후 꼭 개선하고싶다.
# 파이썬 풀이 정말 거지같다. 시간 초과의 경계에서 있는 것 같은데 심지어 같은 코드도 맞았다 틀렸다 한다;;

# 리스트가 global 없이 접근 가능한 이유?
# 정확히는 idx 변수보단 len. cnt가 적합하다. 이를 수정하자.