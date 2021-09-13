import sys
import heapq

input = sys.stdin.readline

n = int(input())

left = []  # maxheap
right = []  # minheap

for _ in range(n):
    x = int(input())

    if len(left) == len(right):
        heapq.heappush(left, (-x, x)) 
    else:
        heapq.heappush(right, (x, x))

    if right and left[0][1] > right[0][1]:  # 정렬이 어긋났는지 검증
        r = heapq.heappop(right)[1]
        l = heapq.heappop(left)[1]
        heapq.heappush(left, (-r, r))
        heapq.heappush(right, (l, l))

    print(left[0][1])   # left의 루트가 중간값 역할