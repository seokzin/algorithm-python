import sys
 
n  = int(input())

for i in range(n):
  a, b = map(int, sys.stdin.readline().split())
  print(a+b)

# input()을 sys.stdin.readline()으로 바꾸는 습관을 들이는게 좋을까? https://dailyheumsi.tistory.com/32