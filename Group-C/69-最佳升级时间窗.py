# 根据过去一段时间 （1周） 内每小时的平均访问量，确定最佳升级时间窗口

# 时间窗口内累计用户访问量不能超过给定阈值
# 时间窗口必须是连续的 x 小时，最大的 x 为最佳升级时间窗口，x <= 7 * 24 = 168 小时
# 时间窗口允许跨周期，比如从 当前 167 小时，到下一个周期的第 166 小时
# 存在多个相同的时间窗口，返回下标最小的

# 每个周期的访问量一致
# 所以可以将数组扩展一倍，变成 336 小时 -> 整个周期不超过 168 小时
# 使用滑动窗口，时间复杂度 O(n)

threshold = int(input())
accesses = list(map(int, input().split()))

left = 0
right = 0

max_width = -1
result_left = -1
sum = 0
while left < 168: # 最大窗口 168
    # 判断依据是平均访问量 。。。
    sum += accesses[right % len(accesses)]
    width = right - left + 1
    if sum <= threshold:
        right += 1
    else:
        if max_width < width - 1:
            max_width = width - 1
            result_left = left
        # 尝试收缩窗口，直到满足条件
        while left < right and left < 168:
            sum -= accesses[left]
            left += 1
            width -= 1
            if sum <= threshold:
                break
        right += 1


print(result_left, result_left + max_width - 1)

