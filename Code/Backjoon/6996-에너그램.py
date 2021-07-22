n = int(input())

for i in range(n):
  a, b = map(str, input().split())

  if sorted(a) == sorted(b):
    print(f'{a} & {b} are anagrams.')
  else:
    print(f'{a} & {b} are NOT anagrams.')