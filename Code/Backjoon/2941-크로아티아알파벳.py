s = input()

arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

cnt = 0

for i in arr:
  s = s.replace(i, '*')

print(len(s))

# 파이썬 문자열 삭제 - strip(양끝에만 해당됨), replace 응용
# 파이썬 문자열은 변경 불가 - 복제 후 대입해야함. 다만 replace를 통해 공백으로 바꾸면 조각난 단어가 만나 새로운 크로아티아 단어가 될 수도 있으니 공백으로 변경은 부적절함