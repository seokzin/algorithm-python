while True:
  num = input()
  pal_num = num[::-1] # num.reverse()

  if num == '0':
    break
  elif num == pal_num:
    print('yes') # 팰린드롬수 O
  else:
    print('no') # 팰린드롬수 X

# 파이썬 리스트 순서 뒤집어 풀기. 메소드에 의존 최대한 말기
# list(input()) - 주의! 빈 리스트에 한글자씩 원소로 삽입하는 것
# ex) ['3', '5', '5']