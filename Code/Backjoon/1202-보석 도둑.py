import heapq
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
jewel = []
bags = []
res = 0

for _ in range(n):
    heapq.heappush(jewel, list(map(int, input().split())))

for _ in range(k):
    bags.append(int(input()))

bags.sort()

tmp_jewel = []

for bag in bags:
    while jewel and (bag >= jewel[0][0]):
        heapq.heappush(tmp_jewel, -heapq.heappop(jewel)[1])  # 최대힙

    if tmp_jewel:
        res -= heapq.heappop(tmp_jewel)
    elif not jewel:
        break

print(res)

# 최소 무게의 가방부터 최대 무게의 보석 담는 과정을 반복하면 그게 최대가 된다? -> 어떻게 장담할 수 있지?
# 2차원 리스트도 최소힙은 첫 번째 항목을 우선순위
# 최대힙 원리에 대한 이해가 좀 더 필요하다