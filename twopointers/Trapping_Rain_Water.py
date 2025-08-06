# the water the bars can trap depending on the shortest bar.
# we use two pointers, the left pointer starts from the leftmost bar, and the right pointer starts from the rightmost bar.
# we also use two variables to store the maximum height of the left and right bars.
# the idea is to move the pointer of the shorter bar inward, and for each position, we calculate the area of the water that can be trapped.
# if the current height is greater than the maximum height of the left or right bar, we update the maximum height.
# and the water can be trapped in current position if for the left pointer, the height is greater than the maximum height of the left bar, and for the right pointer, the height is greater than the maximum height of the right bar.
# and we sum up the area of the water that can be trapped in each position.
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trapped = 0

        while left < right:
            # each step, we shift the pointer of the shorter bar inward
            if height[left] < height[right]:
                water_trapped += max(0, left_max - height[left])
                left += 1
                left_max = max(left_max, height[left])
            else:
                water_trapped += max(0, right_max - height[right])
                right -= 1
                right_max = max(right_max, height[right])

        return water_trapped

# the time complexity is O(N) because we only traverse the list once, and the space complexity is O(1) because we only use a few variables to store the maximum height and the water trapped.

# the correctness of this algorithm is, if we meet the case that the highest bar is on the left, and the bars actaully can not trap any water, we will keep moving the right pointer inward, and since the new bar is always higher then the right one, there will be no water collected. So it is reasonable we always move the pointer of the shorter bar inward. For the left bar, if we move it, we will always have a right bar that is higher than it, so we can calculate the trapped water at that position use 'max(0, left_max - height[left])'. As well as for the right bar.
