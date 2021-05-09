def solution(n, lost, reserve):
    re = list(set(reserve)-set(lost))
    lo = list(set(lost)-set(reserve))
    
    for i in re: 
        if i-1 in lo: 
            lo.remove(i-1) 
        elif i+1 in lo: 
            lo.remove(i+1)

    return n - len(lo)

# 제한사항에 힌트가 있다. lost = reserve일 수도 있으니 중복 제거
# 당연히 왼쪽부터 탐색하는게 최선이다.
# remove del 차이 다시금 정리
# for + in이면 결국 O(n^2) 아닌가? 비효율 같긴한데..
# set에 for랑 in이 정상 작동하나?