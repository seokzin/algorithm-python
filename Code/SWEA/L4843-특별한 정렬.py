from collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    deq = deque(sorted(list(map(int, input().split()))))
    arr = []  # 특수정렬 담을 리스트

    for i in range(5):
        arr.append(deq.pop())
        arr.append(deq.popleft())

    print(f"#{tc} ", end="")
    print(*arr)

# 외부 모듈을 지양하는 취지에 어긋나지만,, 덱이 생각나서 한번 보여드릴 겸 썼습니다.