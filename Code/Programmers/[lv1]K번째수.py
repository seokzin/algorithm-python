def solution(arr, cmd):
    ans = []
    
    for i in cmd:
        ans.append(sorted(arr[i[0]-1 : i[1]])[i[2]-1])
    
    return ans

# slice splice 쓰는 법. slice는 어디서 본거지..