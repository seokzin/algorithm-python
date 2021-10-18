# 정렬기준 : 작업시간 길이로 추정

def solution(jobs):
    result = 0

    # 길이순으로 비교 후 재정렬

    list1 = sorted(jobs, key=lambda x: x[1])

    for i in range(len(list1)):
        for j in range(i+1):
            result += list1[j][1]
            # print(result)
        result -= list1[i][0]
        # print(result, '입니다')
    result /= len(list1)

    return result