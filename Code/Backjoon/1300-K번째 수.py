n = int(input())
k = int(input())

start = 1
end = k

while start <= end:
    mid = (start+end) // 2
    cnt = 0

    for i in range(1, n+1):
        cnt += min(mid//i, n) # i행에서 mid 이하의 총 숫자 개수
    
    if cnt >= k:  # 이분탐색 실행
        end = mid - 1
    else:
        start = mid + 1
        
print(end+1)

# cnt 구하는 것이 핵심 로직, 이분 탐색으로 탐색 복잡도를 줄인 것. 이해하느라 무척 힘들었다.