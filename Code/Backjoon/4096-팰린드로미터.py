while True:
  s = input()
  num = s

  if s == '0':
    break

  while True:
    if num == num[::-1]: # 펠린드롬일 때
      print(int(num)-int(s))
      break
    else: 
      num = str(int(num)+1).zfill(len(s)) # num 1 올린 후 앞에 0 추가

# 그리디 -> 브론즈라서 가능한 문제
# 좀 더 가독성 좋았으면 좋았을 듯