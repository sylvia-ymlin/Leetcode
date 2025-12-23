# 根据提示，解出正确的迷底数字
# 输入
# 猜测的次数
# 每次猜测的数字 和对应的提示（A表示位置正确的字数的个数，B表示数字正确但位置错误的个数）

# since only 4-digit, so the combination is limited -> 10^4 = 10000
# we can generate all numbers and check with each guess

from itertools import combinations

n = int(input())
guesses = [input().split() for _ in range(n)]
guesses = [(g, int(h[0]), int(h[2])) for g, h in guesses]

# possible digits for each position
pos = [set(range(10)) for _ in range(4)]

# reduce search space using hints
for g, a, b in guesses:
    if a == 0:
        for i, d in enumerate(g):
            pos[i].discard(int(d))
    if a + b == 0:
        for i, d in enumerate(g):
            d = int(d)
            for s in pos:
                s.discard(d)

# generate candidate numbers
from itertools import product
candidates = [''.join(map(str, p)) for p in product(*pos)]

res = set()
for num in candidates:
    
    s = list(str(num).zfill(4))
    valid = True
    for guess, a, b in guesses:
        cnt = set(s)
        count_a = count_b = 0
        for i in range(4):
            if s[i] == guess[i]:
                count_a += 1
                cnt.discard(s[i])
        count_b = sum(1 for ch in guess if ch in cnt)
        if count_a != a or count_b != b:
            valid = False
            break
    if valid:
        res.add(''.join(s))
    if len(res) > 1:
        break

print(res.pop() if len(res) == 1 else "NA")






