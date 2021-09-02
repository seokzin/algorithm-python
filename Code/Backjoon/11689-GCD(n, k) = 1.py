n = int(input())
res = n

for i in range(2, round(n**0.5)+1):  # 소인수 while로 빠르게 걸러내기
    if n % i == 0:
        while n % i == 0:
            n //= i

        res *= 1 - (1/i)

if n > 1:  # 마지막 소인수 걸러내기
    res *= 1 - (1 / n)  
    
print(round(res))

# 오일러 파이함수를 구현