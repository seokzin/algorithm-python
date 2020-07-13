x = 10
if x == 10:
    print('10입니다.')

# 코드 생략 (pass != continue)
if x == 10:
    pass # 실행할 코드가 없다는 의미

for x in range(10):
    if x == 10:
        continue # 다음 Loop를 돌도록 강제 (Loop문에서 사용)

# 중첩 if문
if x > 5:
    print('5 이상입니다.')

    if x == 10:
        print('10입니다.')

    if x == 15:
        print('15입니다.')

# 입력값 받아서 if문
y = int(input())

if y == 10:
    print('10입니다.')

# else
x = 5
if x == 10:
    print('10입니다.')
else:
    print('10이 아닙니다.')

# None의 Boolean 값은?
if None:
    print('참')
else:
    print('거짓')    # None은 거짓

# 여러개의 조건식 - 중첩 if문과 연관
if x == 10 and y == 20:
    print('참')
else:
    print('거짓')

# elif
if x == 10:             # x가 10일 때
    print('10입니다.')
elif x == 20:           # x가 20일 때
    print('20입니다.')
else:                   # 앞의 조건식에 모두 만족하지 않을 때
    print('10도 20도 아닙니다.')