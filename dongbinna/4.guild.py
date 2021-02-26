# 공포도 - 최대 그룹 수
# n = 모험가 수 / data = 모험가들의 공포도

n = int(input())

data = list(map(int, input().split()))
data.sort()

result = 0
count = 0 # 현재 그룹의 모험가 수

for i in data:
  count += 1

  if count >= i:
    result += 1
    count = 0

print(result)

# 어렵구만