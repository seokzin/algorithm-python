P = 1000000007


def power(a, b):
    if b == 0:
        return 1
    if b % 2:
        return (power(a, b//2)**2 * a) % P
    else:
        return (power(a, b//2)**2) % P


n, k = map(int, input().split())
fac = [1 for _ in range(n+1)]

for i in range(2, n+1):  # 약분 fact 써야 시간초과 안남
    fac[i] = fac[i-1]*i % P

a = fac[n]
b = (fac[n-k] * fac[k]) % P

print(a%P * (power(b, P-2) % P) % P)

# 페르마의 소정리, 제곱 재귀화 등의 수학 개념이 필요
# 범위 초과 에러가 잘 검출 안돼서 힘들었던 문제. % 하나라도 빠지면 안된다.