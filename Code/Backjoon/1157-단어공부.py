from collections import Counter

word = input()
cnt = Counter(word.upper())
max_cnt = -1

for letter in cnt:
  if cnt[letter] > max_cnt:
    max_cnt = cnt[letter]
    max_letter = letter
  elif cnt[letter] == max_cnt:
    max_letter = '?'

print(max_letter)

# 개선: Counter 사용 전 중복 알파벳 제거. but Counter 자체에서 중복은 건너뛰지 않을까?