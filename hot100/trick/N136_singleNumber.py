# 找到只出现过一次的元素，其他元素都出现了两次
# 线性时间复杂度，常量额外空间 -> 位运算
# 两个相同的数 异或 为 0，0 和 任何数异或 是数本身
# 异或运算满足交换律和结合律

# (a^a)^(b^b)^c = c
# a^b^c^a^b -> 可以是任何顺序

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result
