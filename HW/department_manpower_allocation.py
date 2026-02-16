# Department currently needs to complete N requirements, workload size of each requirement is requirements[i]
# Requirements need to be completed within M months
# After manpower allocation, manpower for each month is fixed
# At most 2 requirements can be developed each month
# Minimum manpower required while meeting development requirements

m = int(input().strip())
nums = list(map(int, input().strip().split()))
n = len(nums)

# Group requirements such that the group with largest manpower requirement is minimized
# At least one requirement per month
# At most two
# Problem satisfies that each month can be assigned at least one requirement

# Find max requirement value as lower bound, 2*max(nums) as upper bound
left = max(nums)
right = 2 * left

# Binary search time complexity O(log(max_requirement))
# Check function time complexity O(N)
# Overall time complexity O(N log(max_requirement))

# If using sort + greedy, time complexity O(N log N)

# Problem n is much smaller than max(requirements), so sorting is faster

nums.sort(reverse=True)

# First assign largest m requirements
# Then pair remaining in descending order. We know x is the m-th largest requirement. If we don't assign m+1-th largest requirement to x, it will cause later combinations to be larger

# Sum
idx = m - 1
for i in range(m, n):
    nums[idx] += nums[i]
    idx -= 1

print(max(nums[:m]))
