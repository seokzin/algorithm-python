import math

def solution(pro, spd):
    days = [math.ceil((100-a) / b) for a, b in zip(pro, spd)]
    ans = []
    idx = 0 # 기준
    
    for i in range(1, len(days)):
        if days[idx] < days[i]:
            ans.append(i-idx)
            idx = i
            
    # 마지막 ans 원소는 따로 append 해줘야 한다.
    ans.append(len(days)-idx)
    
    return ans
    
# 리스트 내부 몫 연산은 원소끼리 해야한다. 
# math.ceil 쓰는 방법이 최선인가?
# 배운 것: 기준을 두고 비교하는 방법 + 인덱스를 조정해 리스트 길이처럼 다루기
# 스택, 큐 사용하지 않고 푼게 미스.. 모범 답안 공부하자