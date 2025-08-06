# find the subarrays sum up to k
# we can not assume the array is sorted
# return the number of subarrays

# the problem of two pointers method is, we do not kow when to move the left and right pointers
# we propose a prefix sum method with the hash table
# the prefix sum is the sum of the elements from the start to the current index
# then the sum of a subarray from index i to j is prefix[j] - prefix[i - 1]

from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        # use a dictionary to store the prefix sum and its frequency
        cnt = defaultdict(int)
        prefix_sum = 0
        for x in nums:
            cnt[prefix_sum] += 1
            prefix_sum += x
            # if not exits, will return 0
            count += cnt[prefix_sum - k]
        return count