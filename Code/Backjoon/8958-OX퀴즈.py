n = int(input())
count = 0
score = 0

for i in range(n):
  ans = input()
  # for j in range(len(ans)):
  #   if(ans[j] == 'O'):
  for j in ans:
    if(j == 'O'):
      count += 1
      score += count
    else:
      count = 0
  print(score)
  count = 0
  score = 0

# 개선: 9-10) for i in arr: i로 arr[i] 접근 가능. 시간, 메모리는 같음