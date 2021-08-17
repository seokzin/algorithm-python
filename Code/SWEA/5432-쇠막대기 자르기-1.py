T = int(input())

for tc in range(1, T+1):
    data = input()
    stack = []
    res = 0

    for i in range(len(data)):
        if data[i] == '(': 
            stack.append('(')
        elif data[i] == ')':
            if data[i-1] == '(':  # 레이저일 때
                stack.pop() 
                res += len(stack)
            else: 
                stack.pop()
                res += 1

    print(f'#{tc} {res}')

# cnt가 편하지만 범용적으로 풀기 위해 stack 사용
# 그래도 리팩토링 여지가 많다.