# 1. 다리 길이 배열을 만든다. -> insert를 통해 밀어낸다. 넘는걸 제거한다. 무게가 넘는지 테스트한다. 결국 밀어내는게 핵심 아이디어! 큐vs스택

def solution(bridge_length, weight, truck_weights):
    # 다리 리스트 생성
    que = [0] * bridge_length
    time = 0

    # 다리 리스트가 빌 때(False)까지
    while truck_weights:
        # 다리 무게가 초과X라면 : 끝값제거 + 트럭넣기 + 트럭0값 제거 + 카운트+1
        del que[bridge_length - 1]

        if sum(que) + truck_weights[0] <= weight:
            que.insert(0, truck_weights[0])
            del truck_weights[0]
            time += 1

        # 다리 무게가 초과한다면: 끝값제거 + 다리0추가 + 카운트+1
        else:
            que.insert(0, 0)
            time += 1
    return time + bridge_length

# 느낀점
# 1. 70% 이해하면 디테일 코드 작성이 힘들다.
# 2. 초반엔 강의의 도움으로 풀이 노하우를 익히는게 좋아보인다.
# 3. 더 많이 종이로 고민하자.
# 4. 연습땐 print를 활용하여 과정을 지켜보자
# 5. insert와 append의 성능 차이가 매우 심하다. append를 목표로 코딩하자.