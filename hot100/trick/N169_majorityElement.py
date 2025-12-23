# 时间复杂度 O(n), 空间复杂度 O(1)
# 不额外构造集合，没有嵌套循环

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 选择一个候选众数 x，count 个数
        # 遍历链表，遇到 x，count +1，遇到其他数，count -1
        # 如果 count = 0，选择下一个数作为候选众数
        # 输出遍历完后所维护的候选众数，就是数列的众数

        # 正确性：我们每一次 +1 -1 都消除了数列中两个不同的数，count 的意思代表当前遍历完的数列中，候选数个数和其他所有数的差值
        # 当 count == 0， 前面所有数抵消，开启一个新序列

        res = 0
        count = 0

        for num in nums:
            if count == 0:
                res = num
            elif num == res:
                count += 1
            else:
                count -= 1
        
        return res

# 但是其实排序的时间复杂度更低，众数是中位数
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]