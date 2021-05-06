def solution(par, com):
    for i in par:
        if par.count(i) - com.count(i) == 1:
            return i
            break
        
        if i not in com:
            return i
                
# 처음에 단순하게 풀었다. 딱 봐도 효율성 최악
# 결과: 정확성: 50.0 / 효율성: 0.0
