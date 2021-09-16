from collections import deque

n, l = map(int, input().split())
arr = list(map(int, input().split()))
q = deque()

for i in range(n):
    while q and q[-1] > arr[i]: 
        q.pop()

    q.append(arr[i])

    if i >= l and q[0] == arr[i-l]:  # l 이후 인덱스에선 첫 값의 범위초과를 체크
        q.popleft()

    print(q[0], end=' ')

# 슬라이딩 윈도우. 손코딩으로 이해는 되나 100%는 아님. 