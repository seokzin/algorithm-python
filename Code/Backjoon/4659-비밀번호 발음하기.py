import sys

def is_good_pwd(s):
  vows = 'aeiou'

  if s == 'end':
    sys.exit()

  for i in range(len(s)):
    if s[i] in vows:
      break
  else:  # for문을 완주했다 = 모음이 없었다
    return False

  for i in range(len(s)):
    if i > 0:
      if s[i]==s[i-1] and s[i]!='e' and s[i]!='o':
        return False  # 같은 글자가 두번 올때 (e,o 제외)
    
    if i > 1:
      if s[i] not in vows and s[i-1] not in vows and s[i-2] not in vows:
        return False  # 자음이 3개 올 때
    
      if s[i] in vows and s[i-1] in vows and s[i-2] in vows:
        return False  # 모음이 3개 올 때
      
  return True

while True:
  s = input()

  if is_good_pwd(s):
    print(f'<{s}> is acceptable.')
  else:
    print(f'<{s}> is not acceptable.')

# for-else 문이 절실히 필요했던 문제.. 
# 근데 괜히 함수화해서 코드가 복잡해졌다. 플래그가 더 편했다.