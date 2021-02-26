# 알파벳과 숫자 문자열을 오름차순 정렬 - 숫자는 다 더해서 마지막에

data = input()
result = []
value = 0

for x in data:
  if x.isalpha():
    result.append(x)
  else:
    value += int(x)

result.sort()

if value != 0:
  result.append(str(value))
  # result.append(value)

  print(''.join(result))

# join - 문자열로 구성돼야 작동 / 정수 쓰면 에러: sequence item 3: expected str instance, int found