def solution(sco, k):
    cnt = 0
    
    while min(sco) < k and len(sco) >= 2:
        sco.sort()
        a = sco.pop(0)
        b = sco.pop(0)
        sco.append(a + (2*b))
        cnt += 1
    
    if min(sco) < k:
        cnt = -1
        
    return cnt

# -1을 while에서 어떻게 표현하지?
# 실패: 정확성: 76.2 / 효율성: 0.0