import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = dict(input().split() for _ in range(n))  # arr -> dict 화

for _ in range(m):
    print(dic[input().rstrip()])