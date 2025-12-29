# 给定小写字母构成的字符串 A B
# A 中可能存在重复字母，B 中的字母均不重复
# 从 A 中挑选一些字母构成字符串 B
# 1. 每个位置的字母只能选一次 -> 选了之后直接删除
# 3. 挑选的字母先后顺序不能变

# 输出可以从 a 中挑选出 b 的方案数

# 不断从 a 中寻找 b 的每个字母，找完一组后将对应字母删除，继续寻找下一组，直到找不到为止

from collections import deque


a = input().strip()
b = input().strip()

# 记录 a 中每个字母出现位置的索引
indices = {c: deque() for c in set(a)}
for i, c in enumerate(a):
    indices[c].append(i)

count = 0
while True:
    last_index = -1 # 记录上一个字母的位置
    for c in b:
        if c not in indices:
            print(count)
            exit()
        # 在 indices[c] 中找到第一个大于 last_index 的位置
        while indices[c] and indices[c][0] <= last_index:
            indices[c].popleft()
        if not indices[c]:
            print(count)
            exit()
        else:
            last_index = indices[c].popleft()
    # 成功找到一组 b，计数加 1
    count += 1

print(count)

