h, m = map(int, input().split())

if m < 45:
  h -= 1
  m += 15
else:
  m -= 45

print(24+h if h < 0 else h , m)

# 9) 삼항 연산자 - m 부분도 사용해서 if문 없애고 싶은데 h -1 구현이..