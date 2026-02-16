# Median of two sorted arrays

from typing import List
# Brute force: merge, sort, take median
# Maintain two pointers, find kth smallest element

# Binary search
# Odd: find kth smallest element
# Even: find kth smallest and (k+1)th smallest, take average
# Binary search, we want to find kth smallest
# Based on quicksort idea, find a pivot
# pivot1 = nums1[k/2-1]
# pivot2 = nums2[k/2-1]
# pivot = min(pivot1, pivot2)
# Then number of elements less than pivot in both arrays does not exceed k - 2
# pivot is at most (k-1)th smallest element
# if pivot1 < pivot: can be discarded, cannot be kth smallest, subtract these deleted elements from k; if pivot2 < pivot: likely
# Search in remaining array
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
                    # Discard first half of nums1
                    k -= (mid1 - l1 + 1)
                    l1 = mid1 + 1
                else:
                    # Discard first half of nums2
                    k -= (mid2 - l2 + 1)
                    l2 = mid2 + 1


        # Length after merge
        n = len(nums1) + len(nums2)
        if n % 2 == 1:  # Odd length
            return self.get_kth(nums1, nums2, n // 2 + 1)
        else:  # Even length
            left = self.get_kth(nums1, nums2, n // 2)
            right = self.get_kth(nums1, nums2, n // 2 + 1)
            return (left + right) / 2

        
            

# Partition array
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Median: partition a set into two parts, such that left elements are all smaller than right elements
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # Always put shorter array in nums1
        infinty = float('inf') # Mark
        m, n = len(nums1), len(nums2)
        l, r = 0, m
        # Binary search in nums1 to find partition method
        while l <= r:
            i = (l + r) // 2  # Partition point of nums1
            j = (m + n + 1) // 2 - i  # Partition point of nums2
            # Ensure nums1[:i] and nums2[:j] occupy half of total length
            # Always adjust partition point of nums1, nums2 partition point determined by nums1
            # If even points, then left half is [0, i-1] + [0, j-1] -> (m+n + 1)//2 elements, median

            # nums_im1, nums_i, nums_jm1, nums_j represent nums1[i-1], nums1[i], nums2[j-1], nums2[j]
            # Boundary condition adjustment
            nums_im1 = (-infinty if i == 0 else nums1[i - 1])
            nums_i = (infinty if i == m else nums1[i])
            nums_jm1 = (-infinty if j == 0 else nums2[j - 1])
            nums_j = (infinty if j == n else nums2[j])

            # Correct partition condition: left half all smaller than right half
            if nums_im1 <= nums_j and nums_jm1 <= nums_i:  # Correct partition
                median_left = max(nums_im1, nums_jm1)
                median_right = min(nums_i, nums_j)
                return (median_left + median_right) / 2 if (m + n) % 2 == 0 else median_left
            elif nums_im1 > nums_j: # Left side has part larger than right side, need to shift i left, but not step by step, using binary search
                r = i - 1  # Incorrect partition, adjust nums1 partition point
            else:
                l = i + 1
        
        return 0.0


        
