import sys
sys.setrecursionlimit(10 ** 6)


def pre_order(in_l, in_r, post_l, post_r):
  if in_l > in_r or post_l > post_r: 
    return # 범위 역전시 재귀 탈출

  root = post_order[post_r]
  print(root, end=" ")

  # 좌우 개수 측정
  left = idx[root] - in_l
  right = in_r - idx[root]

  print(left, right)

  # in과 post의 범위 보정
  pre_order(in_l, in_l+left-1, post_l, post_l+left-1) # 좌
  pre_order(in_r-right+1, in_r, post_r-right, post_r-1) # 우


n = int(input())
in_order = list(map(int,input().split()))
post_order = list(map(int,input().split()))

# index() 함수 역할을 한다. 매번 하면 O(n)이 반복되니까
idx = [0] * (n+1)

for i in range(n):
  idx[in_order[i]] = i

pre_order(0, n-1, 0, n-1)

print(idx)

# 풀이: 후위에서 부모를 찾자. 부모 기준으로 중위를 나눈다. 무한반복
# 얘는 DFS가 답인가..? BFS로 풀 수는 있는건가? 둘의 구분이 약하다.
# 아게 최선의 풀이같다. 코드를 바꿀 여지를 도저히 못찾겠다.
# index() 같은건 사전에 선언하는 테크닉을 배웠다.
# 포스팅 하긴 애매하다. 다만 범위 보정 코드를 검증하기 위해 손코딩을 추천한다.
# 인덱스끼리의 덧, 뺏셈이니까 +1, -1 따위의 보정이 필요 없다..13라인 이후