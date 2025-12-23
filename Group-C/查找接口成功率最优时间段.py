# 给出一个数组，找出最长连续子数组，使得平均值小于等于给定值 target。

# 给出所有满足条件的数组下标
# 格式为 start_index-end_index

# 本质上是在找连续区间满足某个约束（平均值 ≤ target），这类问题更自然地用滑动窗口 / 双指针

# 读入数据
target = int(input())
arr = list(map(int, input().split()))

n = len(arr)

res = []
i = 0

while i < n:
    cur_sum = 0
    length = 0
    start = i

    # 向右扩展
    while i < n and (cur_sum + arr[i]) / (length + 1) <= target:
        cur_sum += arr[i]
        length += 1
        i += 1
    
    # 无法再扩展，记录当前区间
    if length > 0:
        res.append(f"{start}-{start + length - 1}")
    
    # 如果进入过 while， length 肯定大于 0，不需要再加 1
    if length == 0:
        i += 1


# 输出结果
if res:
    print(' '.join(res))
else:
    print("NULL")

