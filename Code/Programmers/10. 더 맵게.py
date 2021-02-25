# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 스코빌이 전부 K 이상 되게..
# 섞는 최소횟수 리턴

def solution(scoville, K):
    count = 0

    while min(scoville) < K:
        # pop한다. a=꼴등, b=꼴등다음.
        a = scoville.pop(0)
        b = scoville.pop(0)
        # 섞어서 넣는다.
        scoville.append(a+(b*2))
        # 오름차 정렬한다. # sort와 sorted 정리하기!
        scoville.sort()
        count += 1

    return count