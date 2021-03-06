import sys

n = int(input())
arr = []

for i in range(n):
  arr.append(int(sys.stdin.readline()))

arr.sort()

for i in arr:
  sys.stdout.write(str(i) + '\n')

# 파이썬 정렬 내장함수 - O(nlogn)
# 1. 시간 초과 - PyPy3으로 바꾸고 성공.
# 2. 시간 단축 - stdin, stdout 도입시 1732ms -> 716ms 단축.