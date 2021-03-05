from collections import deque

n = int(input())

deq = deque()
for i in range(1, n+1):
  deq.append(i)

while len(deq) > 1:
  deq.popleft() # 윗 카드 버리기
  deq.append(deq.popleft()) # 윗 카드를 제일 밑으로

print(deq[0])

# 1. 시간초과 - 직접 만들지 말고 큐를 써야겠다. 근데 remove와 append의 성능 차가 어떻길래? 정리하자. https://chaewonkong.github.io/posts/python-deque.html
# 덱과 큐의 차이는? 덱은 양방향 큐다. 