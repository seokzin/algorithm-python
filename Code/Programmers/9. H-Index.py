def solution(citations):
    answer = 0
    for i in range(len(citations)):
        count = 0
        for j in range(len(citations)):
            if citations[j] >= i:
                count += 1
        if count == i:
            answer = i

    return answer