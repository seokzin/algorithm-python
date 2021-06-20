n = int(input())
res = 0 # 예외 고려해 0으로 초기화

for i in range(1, n+1):
  s = i + sum(list(map(int, str(i)))) # 자릿수 합을 더해 분해합 만듦 
  if n == s:
    res = i
    break # 최소 생성자값 호출 위해

print(res)

# 101a + 11b + 2c 등의 역접근은 예외 처리에 리스크가 크다. 브루트 포스는 무식하게!