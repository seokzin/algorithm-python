T = input()
P = input()
pi = [0] * len(P)
res = []  # P가 나타나는 위치

j = 0  # 접두사 위치
for i in range(1, len(P)):
    while j > 0 and P[i] != P[j]:
        j = pi[j-1]  # P[i] P[j] 다를 때 j를 예전 위치로 되돌린다. 
        
    if P[i] == P[j]:
        j += 1
        pi[i] = j

j = 0
for i in range(len(T)):
    while j > 0 and T[i] != P[j]:
        j = pi[j - 1]

    if T[i] == P[j]:
        if j == len(P)-1:
            res.append(i - len(P) + 2)
            j = pi[j]
        else:
            j += 1

print(len(res))
print(*res)

# 문자열 찾기 - KMP 알고리즘 O(T+P) : 일치 안하면 다음 파트까지 점프!
# 알고리즘 자체는 쉽다. 코드를 다시금 해석해보자