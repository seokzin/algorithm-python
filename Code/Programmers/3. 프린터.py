# A를 뽑아 뒤 행렬중 가장 최대값을 APPEND하고(앤서에 담고) A를 맨뒤로 옮김
# B를 뽑아 동일한 작업 진행
# 만약 큰게 없다면? 그놈을 APPEND함

def solution(priorities, location):
    list1 = []

    for i in range(len(priorities)):
        for j in range(1, len(priorities)):
            max = priorities[i]
            # 최대값을 pop해서 append 할 예정
            list1.append(max)
            del priorities)

        return list1.index(location)