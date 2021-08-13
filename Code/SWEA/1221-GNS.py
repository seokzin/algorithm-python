IDX = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}

T = int(input())

for tc in range(1, T+1):
    info = input()
    words = list(input().split())

    words.sort(key=lambda x: IDX[x])

    print(f"#{tc}\n", *words)
