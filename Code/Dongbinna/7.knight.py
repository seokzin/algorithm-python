# 나이트가 이동 가능한 경우의 수

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트의 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
  next_row = row + step[0]
  next_col = col + step[1]

  if next_row >= 1 and next_row <=8 and next_col >= 1 and next_col <= 8:
    result += 1
 
print(result)