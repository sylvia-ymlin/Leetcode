# Select k numbers from array such that their sum is t
# Output number of ways

# Input format
# n t k
# a1 a2 ... an

# DP or DFS. Select or not select. 

def dfs(start: int, rem_k: int, cur_sum: int) -> int:
    # No more items
    if start == n:
        return 0 # Should check if goal reached? 
        # But base case `rem_k == 0` handles success. 
        # If start==n and rem_k > 0, fail.
        # If start==n and rem_k == 0, handled before.
        # Wait, if start==n and rem_k==0, it's captured by `rem_k == 0` check?
        # Let's put `rem_k == 0` check first.
    
    # Selected enough items
    if rem_k == 0:
        return 1 if cur_sum == t else 0
    
    if start == n:
        return 0

    # Pruning: Sum exceeded or not enough items left
    if cur_sum > t or rem_k > n - start:
        return 0
    
    # Do not select current item
    count = dfs(start + 1, rem_k, cur_sum)
    # Select current item
    count += dfs(start + 1, rem_k - 1, cur_sum + nums[start])

    return count

# Read data
input_line1 = input().split()
if not input_line1: exit()
n, t, k = map(int, input_line1)
nums = list(map(int, input().split()))

# Validation
if not(0 < n < 10 and t > 0 and 0 < k <= n): # Constraint n < 10 is very small!
    print(0)
    exit()

# Wait, logic `any(num <= 0)` check in original.
if any(num <= 0 for num in nums):
    print(0)
    exit()

print(dfs(0, k, 0))
