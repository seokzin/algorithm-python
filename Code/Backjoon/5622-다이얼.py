s = input()

arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

t = 0

for i in s:
  for j in arr:
    if i in j:
      t += (arr.index(j) + 3)

print(t)

# for i in list, str.. 등등 가능하다.