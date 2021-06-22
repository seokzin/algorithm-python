def solution(numbers, target):
    n = len(numbers)
    res = 0
    
    def dfs(i, num):
        if i == n:
            if num == target:
                nonlocal res
                res += 1
            return
        else:
            dfs(i+1, num+numbers[i])
            dfs(i+1, num-numbers[i])
            
    dfs(0, 0)
    
    return res

# def 안에서 모두 해결해야하니 모든 값 다 구해보는게 최선인가..
# def 내에 def 선언이 가능하다.
# global은 전역변수 nonlocal은 지역변수