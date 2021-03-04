a, b = map(str, input().split(' '))

print(a[::-1] if a[::-1] > b[::-1] else b[::-1])

# reverse(s) - list에만 사용 가능
# reversed(s) - string에 사용 가능하나 obj를 리턴. join(list)를 해줘야 str으로 출력 가능
# [::-1] - 간편하고 여러 응용이 가능