# Given an integer M and array N, elements in N are consecutive integers, require assembling new array R from elements in N
# 1. Sum of elements in R equals m
# 2. Elements in R can be repeatedly selected from N
# 3. R can have at most 1 element not in N, and must be smaller than any number in N

# Output number of ways to assemble elements

# Read array
nums = list(map(int, input().split()))
# Read M
M = int(input())

# Can use one extra element
extra = min(nums) - 1

# Use backtracking
def backtrack(remaining, i):
    # remaining: remaining sum to be composed
    # i: current index in nums considered
    if remaining == 0:
        return 1 # Found one combination
    if i >= len(nums):
        return 0 # No more elements to choose
    
    if remaining < nums[i]:
        # Can only choose extra element
        if remaining == extra:
            return 1
        else:
            return 0
    
    # Can choose nums[i] or not choose nums[i]
    total_ways = 0
    # Choose nums[i]
    total_ways += backtrack(remaining - nums[i], i)
    # Not choose nums[i]
    total_ways += backtrack(remaining, i + 1)
    
    return total_ways

result = backtrack(M, 0)
print(result)