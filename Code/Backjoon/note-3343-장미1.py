import sys
input = sys.stdin.readline

n, a, b, c, d = map(int, input().split())

# 최대 루프 수
max_num = 1e5

# 초기치 : 1번 풀매수
answer2 = ((n-1) // a+1) * b

# 첫번째 제품 cnt개 강제 구매
cnt = 0
while(cnt <= max_num):    
    num = n - cnt * a
    if num < 0:
        break
    answer3 = cnt * b
    if num % c == 0:
        answer2 = min(answer2, answer3 + ((num//c) * d))
        break
    # 남은 물건 첫번째 제품으로 도배
    cnt = cnt + 1
    num = ((num - 1)//c) + 1
    answer2 = min(answer2, answer3 + num * d)

# 두번째 제품 cnt개 강제 구매
cnt = 0
while(cnt <= max_num):    
    num = n - cnt * c
    if num < 0:
        break
    answer3 = cnt * d
    if num % a == 0:
        answer2 = min(answer2, answer3 + ((num//a) * b))
        break
    # 남은 물건 첫번째 제품으로 도배
    cnt = cnt + 1
    num = ((num - 1)//a) + 1
    answer2 = min(answer2, answer3 + num * b)

print(answer2)