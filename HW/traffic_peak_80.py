# Given array, find triplet (i, j, k) such that:
# i < j < k AND arr[i] < arr[j] AND arr[k] < arr[j] (Wait, original said "arr[k] < arr[j]"? Yes)
# Basically j is a peak compared to i and k.
# Minimize k - i.

# Input: nums list

# k - i >= 2

# For every j, find rightmost i on left that is smaller than nums[j]
# and leftmost k on right that is smaller than nums[j]
# Wait. To minimize k - i, we want i as large as possible (closer to j) and k as small as possible (closer to j).
# So for fixed j, we want:
# i < j: largest index s.t. nums[i] < nums[j]
# k > j: smallest index s.t. nums[k] < nums[j] (Wait, original code comment says "nums[k] < nums[j]"?)
# Let's check original: "arr[i] < arr[j] and arr[k] < arr[j]".
# Yes.
# To minimize k-i, we want i close to j (from left), k close to j (from right).
# So:
# Left side: Find nearest index i < j with nums[i] < nums[j].
# Right side: Find nearest index k > j with nums[k] < nums[j].
# Original code comment: "Find rightmost i on left smaller than nums[j]". Yes.
# "Find leftmost k on right smaller than nums[j]". Yes.
# Use Monotonic Stack?
# Code uses stack to find "next smaller element" or similar.
# Left pass: `while stack and nums[stack[-1]] >= nums[j]: stack.pop()`.
# This maintains a strictly increasing stack?
# No, if we pop elements >= current, stack top is the nearest element < current on left.
# Because stack stores indices.
# If `nums[top] >= nums[current]`, top cannot be the "nearest smaller" for current?
# Wait. If top >= current, top is NOT smaller. Remove it?
# But top might be needed for future elements?
# If we want nearest smaller to the left:
# Stack should store indices of values.
# If we encounter strictly smaller value, it's a candidate.
# Standard "Nearest Smaller Element" algorithm:
# Maintain stack of increasing values.
# For current x:
# Pop all elements >= x.
# The element remaining on stack is the nearest smaller element to the left.
# Push x.
# Why? Because any element y >= x that was to the left of x is now "blocked" by x for any future queries.
# Any z to the right, if it looks for smaller on left, x is closer than y (and x <= y).
# So yes, standard monotonic stack (increasing).
# The code implementation matches this logic exactly.

nums = list(map(int, input().split()))

n = len(nums)
min_diff = float('inf')

# Two passes

# Left to right: find nearest smaller on left
left_smaller = [-1] * n
stack = []
for j in range(n):
    # Pop larger or equal elements
    while stack and nums[stack[-1]] >= nums[j]:
        stack.pop()
    
    if stack: # Top is nearest smaller
        left_smaller[j] = stack[-1]
    else:
        left_smaller[j] = -1
    stack.append(j)

# Right to left: find nearest smaller on right
right_smaller = [-1] * n
stack = []
for j in range(n-1, -1, -1):
    while stack and nums[stack[-1]] >= nums[j]:
        stack.pop()
    
    if stack: 
        right_smaller[j] = stack[-1]
    else:
        right_smaller[j] = -1
    stack.append(j)

# Calculate min k - i
# Here i is left_smaller, k is right_smaller.
# Wait. The triplet is i < j < k.
# Current j is the peak.
# i must be left_smaller[j]. k must be right_smaller[j].
# So diff = k - i.
for j in range(n):
    i = left_smaller[j]
    k = right_smaller[j]
    if i != -1 and k != -1:
        min_diff = min(min_diff, k - i)

if min_diff == float('inf'):
    print(-1)
else:
    print(min_diff)
