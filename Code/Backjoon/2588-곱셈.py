a = int(input())
b = list(map(int, input()))

print(a * b[2])
print(a * b[1])
print(a * b[0])
print(a * (b[0]*100 + b[1]*10 + b[2]))

# 2, 7) N의 자리 추출은 %을 통해 몫으로 출력해도 되는데 list로 복잡하게 풀었다.