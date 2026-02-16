# Find the element that appears only once, all other elements appear twice
# Linear time complexity, constant extra space -> Bitwise operation
# Two identical numbers XOR to 0, 0 XOR any number is the number itself
# XOR operation satisfies commutative and associative laws

# (a^a)^(b^b)^c = c
# a^b^c^a^b -> can be in any order

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            result ^= num

        return result
