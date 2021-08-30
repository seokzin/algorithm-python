prime = [1 for _ in range(1000000)]

for i in range(2, int(1000000**0.5) + 1):  # 에라토스테네스의 체
    if prime[i]:
        for j in range(i*2, 1000000, i): 
            prime[j] = 0

while True:
    n = int(input())

    if n == 0: 
        break

    for i in range(3, 1000000):
        if prime[i]:
            if prime[n-i]:
                print(f"{n} = {i} + {n-i}")
                break

# 에라토스테네스의 체로 소수 테이블 구축
# 9020 문제와 같음. 추후 개선하자