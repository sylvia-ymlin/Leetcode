# 两个中序数组的中位数

from ast import List
# 暴力解：归并、排序、取中位数
# 维护两个指针，找到第k小的元素

# 二分查找
# 奇数：找第k小的元素
# 偶数：找第k小和第k+1小的元素，取平均值
# 二分查找，我们要找 第 k 小
# 基于快排的思想，找到一个 pivot
# pivot1 = nums1[k/2-1]
# pivot2 = nums2[k/2-1]
# pivot = min(pivot1, pivot2)
# 则 两个数组中小于 pivot 的元素个数不超过 k - 2
# pivot 最大是 第 k-1 小的元素
# if pivot1 < pivot: 可以剔除，不会是第 k 小的元素，从 k 中减去删除的这些元素； if pivot2 < pivot: 同理
# 在剩余数组中查找
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_kth(self, k: int) -> float:
            l1, l2 = 0, 0
            while True:
                if l1 == len(nums1):
                    return nums2[l2 + k - 1]
                if l2 == len(nums2):
                    return nums1[l1 + k - 1]
                if k == 1:
                    return min(nums1[l1], nums2[l2])
                
                mid1 = l1 + k // 2 - 1
                mid2 = l2 + k // 2 - 1

                pivot1 = nums1[mid1] if mid1 < len(nums1) else float('inf')
                pivot2 = nums2[mid2] if mid2 < len(nums2) else float('inf')
                
                if pivot1 < pivot2:
                    # 剔除 nums1 的前半部分
                    k -= (mid1 - l1 + 1)
                    l1 = mid1 + 1
                else:
                    # 剔除 nums2 的前半部分
                    k -= (mid2 - l2 + 1)
                    l2 = mid2 + 1


        # 合并后长度
        n = len(nums1) + len(nums2)
        if n % 2 == 1:  # 奇数长度
            return self.get_kth(nums1, nums2, n // 2 + 1)
        else:  # 偶数长度
            left = self.get_kth(nums1, nums2, n // 2)
            right = self.get_kth(nums1, nums2, n // 2 + 1)
            return (left + right) / 2

        
            

# 划分数组
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 中位数：将一个集合划分为两个部分，使得左边的元素都小于右边的元素
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # 始终将较短的数组放在 nums1
        infinty = float('inf') # 标记
        m, n = len(nums1), len(nums2)
        l, r = 0, m
        # 在 nums1 中二分查找，寻找划分的方式
        while l <= r:
            i = (l + r) // 2  # nums1 的划分点
            j = (m + n + 1) // 2 - i  # nums2 的划分点
            # 保证 nums1[:i] 和 nums2[:j] 占据总长度的一半
            # 始终调整的是 nums1 的划分点，nums2的划分点根据 nums1的划分点确定
            # 如果有偶数点，则 左半边是 [0, i-1] + [0, j-1] -> (m+n + 1)//2 个元素，中位

            # nums_im1, nums_i, nums_jm1, nums_j 分别表示 nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            # 边界条件调整
            nums_im1 = (-infinty if i == 0 else nums1[i - 1])
            nums_i = (infinty if i == m else nums1[i])
            nums_jm1 = (-infinty if j == 0 else nums2[j - 1])
            nums_j = (infinty if j == n else nums2[j])

            # 划分正确的条件: 左半部分都小于右半部分
            if nums_im1 <= nums_j:  # 划分正确
                median_left = max(nums_im1, nums_jm1)
                median_right = min(nums_i, nums_j)
                l = i + 1 # 划分正确，尝试更大的 i
            else: # 左边存在大于右边的部分，需要左移 i，但不是一步一步，而是 二分
                r = i - 1  # 划分不正确，调整 nums1 的划分点
        
        return (median_left + median_right) / 2 if (m + n) % 2 == 0 else median_left


        
