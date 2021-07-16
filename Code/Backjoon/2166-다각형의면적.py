n  = int(input())
a = []
for i in range(n):
  a.append(list(map(int, input().split())))
    
a.append(a[0]) # 첫 꼭지점을 리스트 마지막에 추가

res = 0

for i in range(n):
  res += a[i][1]*a[i+1][0] - a[i][0]*a[i+1][1]

print(abs(res/2))

# wikihow -> 다각형 넓이 구하기 사용.. 너무 수학문제