gen_set = []

for i in range(1, 10001):
    gen_set.append(i + sum(list(map(int, str(i)))))  # 9786 -> { 9, 7, 8, 6 } 만든 후 sum 하는 과정

res = sorted(list(set(range(1, 10001)) - set(gen_set)))

print(*res, sep='\n')