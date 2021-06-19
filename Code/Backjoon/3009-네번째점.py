x = []
y = []

for _ in range(3):
  a, b = map(int, input().split())
  x.append(a)
  y.append(b)

# 1번 언급된 x, y 좌표쌍이 4번째 좌표가 된다.
for i in range(3):
  if x.count(x[i]) == 1:
    res_x = x[i]
  if y.count(y[i]) == 1:
    res_y = y[i]

print(res_x, res_y)

# 다른 방법 - 대각선 중앙 값을 알아낸다. 대각선 요소는 반드시 존재하니까..