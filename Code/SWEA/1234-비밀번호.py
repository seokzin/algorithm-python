for tc in range(1, 11):
    stack = []
    N, words = input().split()

    for word in words:
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)

    print(f'#{tc} ', *stack, sep='')