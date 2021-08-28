from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    D = ((1, 0), (0, 1), (-1, 0), (0, -1))

    q = deque()
    q.append([0, 0])
    visit[0][0] = 1

    dq = [deque() for i in range(26)]
    res = 0

    while q:
        x, y = q.popleft()

        for d in D:
            nx, ny = x+d[0], y+d[1]

            if 0 <= nx < h+2 and 0 <= ny < w+2:                
                if arr[nx][ny] == '*':
                    continue
            
                if not visit[nx][ny]:
                    visit[nx][ny] = 1

                    if arr[nx][ny] == '$':
                        res += 1

                    elif 'A' <= arr[nx][ny] <= 'Z': # 문일 때
                        d = ord(arr[nx][ny]) - ord('A')
                        if not keys[d]:
                            dq[d].append([nx,ny])
                            continue

                    elif 'a' <= arr[nx][ny] <= 'z': # 열쇠인 경우
                        k = ord(arr[nx][ny]) - ord('a')
                        keys[k] = 1

                        while dq[k]:
                            kx, ky = dq[k].popleft()
                            q.append([kx, ky])
                    
                    q.append([nx,ny])
    return res
                

for _ in range(int(input())):
    h, w = map(int,input().split()) 
    arr = []
    visit = [[0]*(w+2) for _ in range(h+2)]

    arr.append(list('.' * (w+2)))  # 빌딩 밖을 드나들 수 있어 패딩 추가
    for _ in range(h):
        arr.append(list('.' + input() + '.'))  # append는 한줄 for문이 안되나보다..
    arr.append(list('.' * (w+2)))

    keys = [0] * 26
    key_input = input().strip()  # 공백이 함께온다.

    if key_input != '0':
        for key in key_input:
            keys[ord(key) - ord('a')] = 1

    print(bfs())

# 복잡하다. 다시 풀어볼 문제