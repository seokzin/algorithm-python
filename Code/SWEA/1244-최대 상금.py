def swap():
    case = set([n])  # 중복 제거로 가지치기

    for _ in range(int(k)):
        tmp = set()
        
        while case:
            s = case.pop()
            s = list(s)  # str -> list 로 swap 가능하게 만듦

            for i in range(len(n)):
                for j in range(i+1, len(n)):
                    s[i],s[j] = s[j],s[i]
                    tmp.add(''.join(s))  # 다시 list -> str으로 저장
                    s[i], s[j] = s[j], s[i]  # 백트래킹

        case = tmp

    return sorted(list(case))[-1]  # 정렬된 마지막 값 = 최대값


for tc in range(1, int(input())+1):
    n, k = input().split()

    print(f'#{tc}', swap())