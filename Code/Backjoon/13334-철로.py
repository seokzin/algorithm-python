import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [sorted(list(map(int, input().split())))  for _ in range(n)]
arr.sort(key=lambda x: x[1])  # end 기준 정렬
d = int(input())
res = 0
hq = []

for s, e in arr:
    if s+d >= e:  # 막대 범위 안에 있다면 hq에 넣어 s순 정렬
        heapq.heappush(hq, s)
        
    while hq and hq[0]+d < e:
        heapq.heappop(hq)  # 벗어나는 것들은 빼주기

    res = max(res, len(hq))

print(res)