from itertools import combinations

n, s = map(int, input().split())
nums = list(map(int, input().split()))
left = nums[:n//2]
right = nums[n//2:]
cnt = 0

left_sum = []
for i in range(1, n//2+1):
    cases = list(combinations(left, i))
    for case in cases:
        pre_sum = sum(case)
        if pre_sum == s:
            cnt += 1
        left_sum.append(pre_sum)

right_sum = []
for i in range(1, n//2+2):
    cases = list(combinations(right, i))
    for case in cases:
        pre_sum = sum(case)
        if pre_sum == s:
            cnt += 1
        right_sum.append(pre_sum)

left_sum.sort()
right_sum.sort(reverse=True)  # 둘다 오름차 정렬 아닌가? 왜 뒤집지?

i = 0
j = 0

while i < len(left_sum) and j < len(right_sum):
    p = left_sum[i] + right_sum[j]
    if p > s:
        j += 1
    elif p < s:
        i += 1
    else:
        ls, rs = 1, 1
        left_idx = i + 1
        right_idx = j + 1
        while left_idx < len(left_sum) and left_sum[left_idx] == left_sum[i]:
            ls += 1
            left_idx += 1
        while right_idx < len(right_sum) and right_sum[right_idx] == right_sum[j]:
            rs += 1
            right_idx += 1

        i = left_idx
        j = right_idx
        cnt += ls*rs
print(cnt)

# 부분합 + 투포인터의 융합 문제... 진짜 어렵다
# 부분합 노가다 하면 최대 2^20 승인데 조합 모듈을 쓴건 조금 아쉽다.
# 추후 무조건 개선해야 할 문제..