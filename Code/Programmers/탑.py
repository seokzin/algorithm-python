def solution(heights):
    answer = [0] * len(heights)
    # 좌로 이동하며 최초로 큰 값이 나오면 그 값의 인덱스를 정답배열에 저장

    for i in range(1, len(heights)):
        for n in reversed(range(i)):
            if heights[n] > heights[i]:
                answer[i] = n + 1
                break

    return answer

# 느낀점
# 1. 빈 리스트에 append 식으로 풀면 좋을 것 같은데.. 나중에 시도해보자.