def solution(par, com):
    par.sort()
    com.sort()
    
    # for i in range(len(com)):
    #     if par[i] != com[i]:
    #         return par[i]
    # return par[-1]

    for i, j in zip(par, com) :
        if i != j :
            return i
    return i[-1]
                
# 지울 필요가 있나? par에 있고 com에 없는 값만 찾으면 됨
# zip(a, b) = 동일한 개수의 두 자료형을 순서대로 짝지어 튜플로 묶는다. 크기가 다를시 나머지 인덱스는 제외한다. 근데 실전에서 zip을 생각할 수 있을까? 참고만 하자.
# zip과 이전 코드의 성능 차이는 거의 없다.