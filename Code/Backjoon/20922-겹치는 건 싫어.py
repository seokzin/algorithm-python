n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = [0] * 100001 # 개수 카운팅
start,end = 0,0
res = 0 # 최대 수열 길이 저장

for i in range(n):
  num = arr[i]
  cnt[num] += 1

  while cnt[num] > k: 
    cnt[arr[start]] -= 1 # 핵심: start 옮기면서 cnt 감소해줘야함
    start += 1

  end += 1
  res = max(res, end-start)

print(res)

# 투포인터(O(n)) + cnt 관리(cnt 배열)
# []*100 = [] 이 나온다. 조심
# indexError -> 대부분 range 초과. 경계값 테스트 하자
# 틀린 이유: cnt[start] X -> cnt[arr[start]] O