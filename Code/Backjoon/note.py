n, m = map(int, input().split())

arr = []

for i in range(n):
  arr.append(input())

for i in range(m):
  quiz = input()

  if str(type(quiz)) == "<class 'int'>":
    print(arr[quiz])
  else: # type = str
    print(arr.index(quiz))