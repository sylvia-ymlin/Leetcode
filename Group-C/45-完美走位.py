# 长度为 4 的倍数的字符串，仅包含 WASD 四种字符

# 读入字符串
s = input().strip()
n = len(s)
# 统计各个字符的数量
# 目标个数
target = n // 4
count = {'W':-target, 'A':-target, 'S':-target, 'D':-target}
for c in s:
    count[c.upper()] += 1

extra_chars = {c:cnt for c, cnt in count.items() if cnt > 0}

if not extra_chars:
    print(0)
    exit()

def can_shrink():
    for c, cnt in extra_chars.items():
        if mem[c] < cnt:
            return False
    return True

# 使用滑动窗口，寻找最短子串，统计窗口内包含的多余字符恰好 == extra_chars
left = right = 0
res = n # 最短子串长度，初始为 n
mem = {c:0 for c in extra_chars}
while right < n:
    char_r = s[right].upper()
    if char_r in extra_chars:
        mem[char_r] += 1
    while can_shrink() and left <= right:
        res = min(res, right - left + 1)
        char_l = s[left].upper()
        if char_l in extra_chars:
            mem[char_l] -= 1
        left += 1
    # 退出循环时, left 指向的子串不再满足条件，继续扩展右边界
    right += 1

print(res)