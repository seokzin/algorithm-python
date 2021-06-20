t = int(input())

for _ in range(t):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())

  d = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
  
  r_sum = r1 + r2
  r_dif = abs(r1 - r2)

  if d == 0 and r1==r2:
    print(-1)
  elif r_sum == d or r_dif == d: # 외접 or 내접
    print(1)
  elif r_dif < d < r_sum: # 서로 다른 두 점
    print(2)
  else:
    print(0)

# if문 위치 선정이 중요하다. 예외를 위에 둔다던가.. -1을 3번째에 두니까 틀렸다고 나온다. 정수와 실수 비교의 오차라고 예상은 한다.. 
# 이해 안가네.. 두 점 좌표가 같을 때 6 라인이 d > 0 가 될수도 있다는 말?