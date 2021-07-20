n = int(input())
pwds = []
res = ''

for _ in range(n):
  pwds.append(input())

for pwd in pwds:
  if pwd[::-1] in pwds:
    res = pwd

print(len(res), res[len(res)//2])