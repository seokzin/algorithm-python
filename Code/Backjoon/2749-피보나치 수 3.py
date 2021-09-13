n = int(input())

def fibo(n):
    a, b = 0, 1

    for _ in range(n):
        a, b = b % 1000000, (a+b) % 1000000  # 동시 할당

    return a 

print(fibo(n % (15*(10**5))))

# 원래는 행렬을 통해 구하는 것이 정석..
# 그러나 피보나치는 15*10^n-1 마다 피사노 주기가 존재. 날먹..