n = int(input())

li = list(map(int, input().split()))

li2 = sorted(set(li))

dic = { li2[i] : i for i in range(len(li2)) }
# dic = { val: idx for idx, val in enumerate(li2)}

for i in li:
  print(dic[i], end= " ")

# set에 정렬을 했는데 결과값은 list가 나오는 이유?
# enumerate로 인덱스 붙이기 가능 - 튜플로 생성됨. 다만 6라인 보다 쪼금 느렸다.