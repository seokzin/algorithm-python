import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
  for j in range(n):
    # arr[i][j] 더하는 이유: 사각형 관점으로 생각하면 우측 모서리 1x1 사각형
    dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + arr[i][j]

for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])

# 첫 방식 - 매 행마다 부분sum하여 토탈 내기 -> 시간 초과 o(n2)니까
# 둘째 방식 - dp마다 부분합 저장해두고 쓰기. 좌표를 예외
# 투 포인터 알고리즘이 뭐지?
# dp를 n+1로 하는 이유. x1, y1이 0일때 예외 처리가 쉬우니까
# 2차원 arr 한줄로 받는 방법은 참고할 만 한듯
# 배열 선언에 따라 통째로 변하는 것은 깊은, 얕은 복사와 관련
# dp 에 첫 행열을 0으로 하는 이유 -> 1 1 4 4 같은 케이스를 대비해서.. 굳이 dp에 0값 제거하려 했다가 훨씬 복잡해짐
# 이게 sys.readline 안써서 시간초과가 나다니.. readline은 어떤 케이스에서 효율이 좋을까? split한 순간에도 효과가 좋나?