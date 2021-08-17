T = int(input())

for tc in range(1, T+1):
    a, b = input().split()
    a = a.replace(b, '_')  # B단어 모두 _ 로 대체

    print(f'#{tc}', len(a))

# replace가 너무 강력한 메서드입니다.
# 정석적으로 푸는게 더욱 좋을 것 같습니다.