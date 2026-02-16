# Arrange a group of people heights in order: Tall, Short, Tall, Short...
# Output arranged heights
# Adjacent can be equal

# Strategy: Traverse, if index is even/odd check condition and swap with next if needed.
# Index 0 (even) -> Should be Short? Or Tall?
# Problem says "Tall, Short, Tall, Short".
# Index 0: Tall. Index 1: Short.
# Odd index (1, 3...): Short -> Should be <= next (Tall).
# Even index (0, 2...): Tall -> Should be >= next (Short).
# Original code comments: "Odd index requires not smaller than next? Even requires not larger?"
# Wait.
# "Tall, Short, Tall, Short"
# 0 (Tall) > 1 (Short). 1 (Short) < 2 (Tall). 2 (Tall) > 3 (Short).
# So:
# Even index i: nums[i] should be >= nums[i+1]. If nums[i] < nums[i+1], swap.
# Odd index i: nums[i] should be <= nums[i+1]. If nums[i] > nums[i+1], swap.
# Original code:
# `if i % 2 == 0: if nums[i] < nums[i+1]: swap` -> Even index ensures >= next. Correct.
# `else: if nums[i] > nums[i+1]: swap` -> Odd index ensures <= next. Correct.

# Pre-check: "Determine if current index is odd or even"
# Also explicit Check `if nums[0] < nums[1]: swap`. This ensures start is Tall?
# Yes, because index 0 is first "Tall".
# The loop starts from 1. 

try:
    nums = list(map(int, input().split()))
except:
    print([])
    exit()

if not nums:
    print([])
    exit()

# Ensure first relationship (0 vs 1) matches Pattern
# Pattern: Tall, Short...
# So 0 > 1.
if len(nums) > 1 and nums[0] < nums[1]:
    nums[0], nums[1] = nums[1], nums[0]

# Loop from 1?
# Previous logic:
# 0>1. Next relation 1 vs 2.
# 1 is Short. 2 is Tall. So 1 < 2.
# i=1 (Odd). Check nums[i] < nums[i+1]?
# If nums[1] > nums[2], swap.
# This matches `else` branch.
for i in range(1, len(nums)-1):
    if i % 2 == 0: # Even, should be Tall (> next)
        if nums[i] < nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
    else: # Odd, should be Short (< next)
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]

print(' '.join(map(str, nums)))