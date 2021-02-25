# #가장 큰 수 = 가장 큰 글자를 정렬한 것
#두글자를 정렬하면 가장 큰쪽으로 간다는 문제 해결해야함!

#무식한 방법 = 모든 경우의 수 나열해서 그중 max한다. - 시간초과
#그나마 나은 방법 = 앞글자끼리 비교해서 정렬한후 2글자에 대해 정렬한다.
# !!!!근데 십의자리가 다음 일의자리보다 커야되는 그런 조건이 까다로워서 무식한 방법이 날듯도 하고 - 이걸 해결하는게 핵심. 글자수 맞춰서 비교한다는 아이디어? 굿

#아니면 전부 리스트화해서 [2] [2,1]...
#인덱스 0에 대해 소팅하고 인덱스 1에 대해 소팅하는 식도 괜찮을듯

#string에서는 대소 비교가 일반 숫자랑은 다르기 때문에 가능한 코드이다.

# 특수 소팅을 해야한다. (어떻게 하면 9 > 30, 3>30을 알수있나?)

# lambda 사용법을 알자

def solution(numbers):
    # 글자수 통일한 특수 리스트 생성
    list1 = list(map(str, numbers))

    # for i in range(len(numbers)):
    #     list1[i] *= int(6/len(list1[i]))

    sorted(list1, key=lambda x: x*(6/len(list[x])))
    # list1.sort(reverse=True)

    return list1

print(solution([3, 30, 34, 5, 9]))

