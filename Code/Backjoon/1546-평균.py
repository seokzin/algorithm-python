n = int(input())

sco = list(map(int, input().split(' ')))
fake_sco = list(map(lambda x: x / max(sco) * 100, sco)) # 람다함수로 코드 단축 가능!

print(sum(fake_sco) / n)

# 기본 리스트 함수엔 평균 메소드가 없다.
# 3) 4라인에 한 줄로 통합도 가능해보이는데 아직은 어려울 듯