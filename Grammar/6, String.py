x = 'hello'
print(x) # 'hello'

# 문자열 표현 방법 (한줄)
'hello'
"hello"
'''hello'''
"""hello"""

# 문자열 표현 방법 (여러줄)
'''hello
every
one'''

"""hello
every
one"""

'hello\nevery\none'

# 문자열 안에 작은, 큰 따옴표 포함하기
"i'm" # i'm
'"hello"' # "hello"
'i\'m' # i'm


# 문자열 응용

# replace : 문자열 바꾸기
'Hello, world!'.replace('world', 'Python') # 'Hello, Python!'

# translate : 문자 바꾸기 - 테이블 형식
table = str.maketrans('aeiou', '12345')
'apple'.translate(table) # '1ppl2' / a=1 e=2 i=3 o=4 u=5

# split : 문자열 분리
'apple pear grape pineapple orange'.split() # 공백 기준 / ['apple', 'pear', 'grape', 'pineapple', 'orange']
'apple, pear, grape, pineapple, orange'.split(', ') # , 기준 / ['apple', 'pear', 'grape', 'pineapple', 'orange']

# join : 리스트 연결
' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange']) # 'apple pear grape pineapple orange'
'-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']) # 'apple-pear-grape-pineapple-orange'

# 대소문자 변환
'python'.upper() # 'PYTHON'
'PYTHON'.lower() # 'python'

# 공백 삭제
'   Python   '.lstrip() # 'Python   ' / 좌측 공백 삭제
'   Python   '.rstrip() # '   Python' / 우측 공백 사겢
'   Python   '.strip() # 'Python' / 양측 공백 삭제

# 특정 문자 삭제
', python.'.lstrip(',.') # ' python.' / 좌측의 콤마 또는 점 삭제
', python.'.rstrip(',.') # ', python' / 우측의 콤마 또는 점 삭제
', python.'.strip(',.') # ' python' / 양측의 콤마 또는 점 삭제

# tip) 특수 문자 삭제 메소드
import string

', python.'.strip(string.punctuation) # string.punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# 정렬
'python'.ljust(10) # 길이 10 만든 뒤 좌측 정렬 / 'python    '
'python'.rjust(10) # 길이 10 만든 뒤 우측 정렬 / '    python'
'python'.center(10) # 길이 10 만든 뒤 가운데 정렬 / '  python  '

# zfill(길이) : 길이에 맞춰 문자열 왼쪽에 0 채우기
'35'.zfill(4) # 길이 4가 되도록 앞을 0으로 채움

# 문자열 위치 찾기
# find : 문자열 위치 찾기 - 없으면 -1 반환
'apple pineapple'.find('pl') # 2
'apple pineapple'.find('xy') # -1

# rfind : 오른쪽부터 찾기
'apple pineapple'.rfind('pl') # 12

# index : 문자열 위치 찾기 (= find) - 없으면 에러
'apple pineapple'.index('pl') # 2

# rindex : 오른쪽부터 찾기 (= rfind)
'apple pineapple'.rindex('pl') # 12

# count : 문자열 개수 세기
'apple pineapple'.count('pl') # 2


# 문자열 서식 지정자 - '%자료형'
name = 'maria'
'I am %s.' % name # 'I am maria.'

'I am %d years old.' % 20 # 'I am 20 years old.'

'%f' % 2.3 # '2.300000'
'%.3f' % 2.3 # '2.300'

'Today is %d %s.' % (3, 'April') # 'Today is 3 April.'

# 문자열 정렬
'%10s' % 'python' # '    python'

# format : 서식 지정자보다 간단한 방식
'Hello, {0}'.format(100) # 'Hello, 100'
'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6) # 'Hello, Python 3.6 Script'
'{0} {0} {1} {1}'.format('Python', 'Script') # 'Python Python Script Script'
'Hello, {language} {version}'.format(language='Python', version=3.6) # 'Hello, Python 3.6'

# %0개수d : 숫자 개수 맞추기
'%03d' % 1 # '001'
'%08.2f' % 3.6 # '00003.60'


