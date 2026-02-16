# Time complexity O(n), Space complexity O(1)
# Do not construct extra set, no nested loops

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Choose a candidate majority element x, count its occurrences
        # Traverse list, if encounter x, count +1, if another number, count -1
        # If count = 0, choose next number as candidate majority element
        # Output candidate majority element maintained after traversal, is the majority element of the sequence

        # Correctness: Each +1 -1 cancels out two different numbers in the sequence, count represents the difference between the candidate number count and all other numbers in the currently traversed sequence
        # When count == 0, all previous numbers cancel out, start a new sequence

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

# However, sorting time complexity is lower, majority element is the median
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]