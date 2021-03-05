s = input()

words = s.split(' ')
while '' in words:
  words.remove('')

print(len(words))

# 실패 요인
# 1. 런타임 에러: if문 - str 앞 뒤 공백시 count 1 감소
# 2. 문법: if -> while 해야 공백 한 개 이상 제거 가능