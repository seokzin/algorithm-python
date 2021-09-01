n = int(input())
res = [0] * 10

units = 1  # 10의 제곱 단위 자릿수

while n != 0:
    while n % 10 != 9:  # 일의 자리가 9가 될 때까지 반복
        for i in str(n):
            res[int(i)] += units
        n -= 1

    if n < 10:
        for i in range(n+1):
            res[i] += units
        res[0] -= units  # 이 연산의 중요성을 모르겠다 (없으면 틀림)
        break

    else:
        for i in range(10):
            res[i] += (n//10 + 1) * units

    res[0] -= units
    units *= 10
    n //= 10

print(*res)

# 규칙을 찾는 수학적 문제
# 규칙이 완벽히 이해 안됨. 나중에 다시 오자