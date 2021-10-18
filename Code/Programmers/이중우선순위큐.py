# [I 16,D 1]	[0,0]
# [I 7,I 5,I -5,D -1]	[7,5]

# if문 이게 최선일까

def solution(operations):
    answer = [0]*len(operations)

    # I라면 뒷값을 넣는다. 근데 순서상 I 앞에 D 뒤에인듯
    for i in range(len(operations)):
        if operations[i][0] == 'I':
            answer.append(operations[i][0].replace('i ', ''))
        # D일때 조건에 맞게 삭제한다. remove가 최선인가?
        elif operations[i] == 'D 1':
            answer.remove(max(answer))
        elif operations[i] == 'D -1': # 이거 분리 안하고 else하면 다 여기로 빠짐
            answer.remove(min(answer))
        else:
            continue

    return [min(answer), max(answer)]

print(solution(["I 16","D 1"]))