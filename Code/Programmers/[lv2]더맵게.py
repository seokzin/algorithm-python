import heapq

def solution(sco, k):
    heapq.heapify(sco)
    
    cnt = 0
    
    while sco[0] < k and len(sco) >= 2:
        heapq.heappush(sco, heapq.heappop(sco) + (2 * heapq.heappop(sco)))
        cnt += 1
        
    if min(sco) < k:
        cnt = -1
        
    return cnt

# heapify를 선언과 동시에 할 순 없을까.
# heapq 메소드는 heapq. 으로 선언해야 하나