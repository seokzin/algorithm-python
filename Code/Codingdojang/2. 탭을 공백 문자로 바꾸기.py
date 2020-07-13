# 탭(Tab) 문자를 공백 4개(4 space)로 바꾸기

# 내 아이디어: replace 메소드 사용
# 강의 아이디어: 내 아이디어

# 코드상의 tab 입력을 '\t'로 인식하지 못하는 것 같다

print('a   b   c   d   e'.replace('\t', ' space ')) # 변화 X
print('a   b   c   d   e'.replace('   ', ' space ')) # 변화 O