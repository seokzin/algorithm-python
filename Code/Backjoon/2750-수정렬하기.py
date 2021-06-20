s = []

n = int(input())

for _ in range(n):
  s.append(int(input()))

s.sort()

print(*s, sep='\n')

# sort() 는 sorted()와 달리 원본을 변경하므로 최선의 풀이는 아닌듯.. 비교해서 포스팅하기