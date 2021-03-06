n = int(input())

for i in range(n):
  arr = input()

  while arr.find('()') != -1:
    arr = arr.replace('()', '')

  if arr != '':
    print('NO')
  else:
    print('YES')

# 아이디어: )를 만났는데 앞에 (가 없었다. - F. 마지막에 뭔가 남아있다 - F. 스택을 이용