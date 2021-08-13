T = 10

for tc in range(1, T+1):
    N = int(input())
    target = input()
    string = input()
    cnt = 0

    cnt = string.count(target)
    
    print(f"#{N} {cnt}")