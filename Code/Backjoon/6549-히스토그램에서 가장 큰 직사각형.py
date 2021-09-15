while True:
    n, *arr = list(map(int, input().split()))  # '*' 활용

    if n == 0:
        break
    
    # 첫 시점, 마지막 시점 체크용 '0'
    arr = [0] + arr + [0]
    stack = [0]
    res = 0
    
    for i in range(1, n+2):
        while stack and arr[stack[-1]] > arr[i]:  # 현재 보다 이전 높이가 높으면 진입
            # 비교할 사각형 index
            cur_height = stack.pop()
            res = max(res, (i-1-stack[-1]) * arr[cur_height])  # 사이에 있는 사각형 개수
        
        stack.append(i)

    print(res)

# 높이가 작아지는 시점이 분기점이다? 알고리즘 생각하기가 어렵다. 다ㅏ시