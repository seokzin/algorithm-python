s = input()

arr = [-1] * 26

for i in range(len(s)):
  arr[ord(s[len(s) - i - 1]) - ord('a')] = len(s) - i - 1

for i in arr:
  print(i, end=' ')

# 다양한 풀이가 존재한다.
# arr.find() - 찾는 문자열 인덱스 반환
# 역순이 아닌 순서대로 가면서 -1이 아니면 continue 하는 식