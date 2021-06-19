s = input()
stack = [] # 연산자 저장 스택
res = ""

for c in s:
  if c.isalpha():
    res += c # 알파벳은 우선순위가 없으므로 결과에 바로 넣는다.
  else:
    if c == '(':
      stack.append(c)
    elif c == '*' or c =='/':
      while stack and (stack[-1] == '*' or stack[-1] == '/'):
        res += stack.pop()
      stack.append(c)
    elif c == '+' or c == '-':
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.append(c)
    elif c == ')':
      while stack and stack[-1] != '(':
        res += stack.pop()
      stack.pop() # '(' 제거

while stack:
  res += stack.pop()

print(res)

# while stack and stack[-1] != '(': 을 while stack[-1] != '(': 로 줄일 수 없나?
# 12번 이해 예시) A/B*C -> AB/C*