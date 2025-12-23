# 一堆长方形积木，截面相同，要堆成一面墙，每层高度相同，问最多能堆多高

# 输入描述：
# 一行积木长度列表，空格分隔

# 输出描述：
# 一行整数，表示最多能堆多高

# 暴力法
# 首先求和
# 墙面的长度，要不是最长积木的长度
# 要不就是最长和最短积木长度之和
# 然后变成两数和问题，要为每个数找到一个搭档，使得两数和等于墙面的长度
# 如果有数没有搭档，则 return -1

from collections import Counter

def can_build(length, blocks, cnt) -> bool:
    """判断是否能用 blocks 堆成每层长度为 L 的墙"""
    for block in blocks:
        if block == length:
            continue
        if cnt[block] == 0:
            continue
        elif cnt[block] > 0:
            complement = length - block
            if cnt[complement] == 0:
                return False
            else:
                cnt[block] -= 1
                cnt[complement] -= 1
    return True

blocks = list(map(int, input().split()))
total_length = sum(blocks)

max_len = max(blocks)
min_len = min(blocks)

cnt = Counter(blocks)
height = -1
if total_length % (max_len) == 0:
    target_len = max_len
    height = total_length // target_len if can_build(target_len, blocks, cnt.copy()) else -1

if height == -1 and total_length % (max_len + min_len) == 0:
    target_len = max_len + min_len
    height = total_length // target_len if can_build(target_len, blocks, cnt.copy()) else -1

print(height)