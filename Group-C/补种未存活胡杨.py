# 一排胡杨树 n 棵，m 棵死亡，可以补种 k 棵
# 补种后，求最长连续存活胡杨树的长度

n = int(input())
m = int(input())
dead_lists = set(map(int, input().split()))
k = int(input())

# 这是一个滑动窗口问题
# 在窗口内死亡树的数量不能超过 k时，扩展右边界
# 当前右边界扩展到不能满足条件时，左边界右移，直到满足条件为止，计算当前窗口长度，更新最大值

left = right = 1 # 给出的树的编号从 1 开始
max_len = 0
dead_count = 0
while right <= n:
    if right in dead_lists:
        dead_count += 1
    while dead_count > k:
        if left in dead_lists:
            dead_count -= 1
        left += 1
    max_len = max(max_len, right - left + 1)
    right += 1
print(max_len)