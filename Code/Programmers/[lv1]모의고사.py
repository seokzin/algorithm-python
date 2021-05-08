def solution(ans):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt = [0, 0, 0]
    sol = []
    
    for i in range(len(ans)):
        if ans[i] == a[i%5]:
            cnt[0] += 1
        if ans[i] == b[i%8]:
            cnt[1] += 1
        if ans[i] == c[i%10]:
            cnt[2] += 1
    
    for i in range(3):
        if cnt[i] == max(cnt):
            sol.append(i + 1)
            
    return sol

# 빼기 해서 0 개수 구하기? 별로 좋은 방법은 아닌듯
