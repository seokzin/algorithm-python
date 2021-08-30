def check(num):
    num = str(num)

    for x in num:
        if x in btn:
            return False
    return True


n = int(input())
m = int(input())
btn = input().split()  # 고장난 버튼
res = abs(100 - n)  # 모든 숫자가 고장난 최악의 경우값

for i in range(1000001):  # 1~5까지 고장났을 땐 6부터 내려오므로. 범위는 최대 100만이다.
    if check(i):
        res = min(res, len(str(i)) + abs(i - n))

print(res)