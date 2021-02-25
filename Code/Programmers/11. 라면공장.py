# if 스톡 < 데이트[k]
# 결과++
# 스톡 += 서플라이[k]

# 스톡을 줄인다는 발상이 아닌, 얼마나 최소로 받아야 k를 넘길 수 있는지 판단.
# 다만 스톡이 0이 되지 않게 장치해야함.
# 마치 연립식인데 result가 스위치처럼 켜지는 식?
# 근데 테스트케이스가 적다..!

def solution(stock, dates, supplies, k):
    result = 0

    for i in range(len(dates)):
        if stock < dates[i]:
            stock += supplies[i]
            result += 1
    return result