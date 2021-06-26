n, k = map(int, input().split())
bag = []
dp = [0 for _ in range(k+1)]

for _ in range(n):
  w, v = map(int, input().split())
  bag.append([w, v])

for i in range(n):
  i_w, i_v = bag[i][0], bag[i][1]

  for j in range(k, 0, -1):
    if j >= i_w:
      dp[j] = max(dp[j], dp[j-i_w]+i_v)

print(dp[-1]) # 마지막 값 = 최대

# 유명한 배낭 문제 - 2중 dp로 풀 수도 있다. (더 직관적이지만 코드가 길어짐)
# 변수명에 대한 고민.. i_w , w(중복사용), wei 중...
# 1차원 dp의 단점 - 거꾸로 반복해야 한다.. 이전 변경이 영향 안가게..
# 이 문제 다시보면서 내가 이해되게끔 리팩토링 해보고 2차원이랑 효율 비교해보자