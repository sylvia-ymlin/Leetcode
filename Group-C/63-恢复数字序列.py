# 给出一个打乱字符顺序的字符串，得到原始的正整数序列

# 输入
# 打乱的字符串 ， 连续正整数序列长度
# 字符串长度不超过 200
# 正整数不超过 1000

s, n = input().split()
n = int(n)

# 判断连续正整数中数的位数
# 一位数： 长度 len(s) / n = 1
# 两位数： 长度 len(s) / n = 2
# 三位数： 长度 len(s) / n = 3
# 四位数只有一位
# 所以如果 1 < len(s) / n < 2 -> 一位数和两位数混合
# 如果 2 < len(s) / n < 3 -> 两位数和三
# 如果 3 < len(s) / n  # 一定有 1000

# 滑动窗口，统计连续正整数序列中各个数字出现的次数，由于 一两位数字本来就很少，所以暴力枚举所有可能的连续正整数序列
from collections import Counter
nums = Counter(s)

left = 1
right = 1
current_count = {'0': 0, '1':0, '2': 0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}  # 数字 -> 出现次数
diff = 0
for i in range(10):
    if current_count[str(i)] != nums.get(str(i), 0):
        diff += 1

while right <= 1000:
    str_right = str(right)
    for ch in str_right:
        current_count[ch] += 1
        if current_count[ch] == nums.get(ch, 0):
            diff -= 1
        if current_count[ch] - 1 == nums.get(ch, 0):
            diff += 1
            # current)_count 超过了 nums, 左移窗口
            while left <= right and current_count[ch] > nums.get(ch, 0):
                str_left = str(left)
                for ch_left in str_left:
                    current_count[ch_left] -= 1
                    if current_count[ch_left] == nums.get(ch_left, 0): # 刚好相等
                        diff -= 1
                    if current_count[ch_left] + 1 == nums.get(ch_left, 0): # 原本相等，现在不等了
                        diff += 1
                left += 1
     # 仅仅保证字符数量相等还不够，还要保证序列长度，因为可能有多个序列字符数量相等
     # 特别是对于 n = 1, 而我们需要输出最小的整数
    if diff == 0 and right - left + 1 == n: 
        break   # 找到符合条件的序列
    right += 1

# 返回序列中最小整数
print(left)