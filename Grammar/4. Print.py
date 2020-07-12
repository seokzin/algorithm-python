# 값을 여러개 출력하기
print(1, 2, 3) # 1 2 3
print('hello', 'python') # hello python

# sep : 값 사이에 문자 넣기
print(1, 2, 3, sep=' 또는 ')
print('hello', 'python', sep='') #hellopython - 공백없애기 가능
print(10, 20, 30, sep='\n') # 줄바꿈

# end : print 출력시 기본 적용되는 줄바꿈 해제
print(1, end='')
print(2, end='')
print(3)
# 123