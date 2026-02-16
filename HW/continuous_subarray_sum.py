# Given a positive integer array, find how many continuous intervals have sum not less than x

# Judging >= x, prefix sum + binary search

n, x = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

import bisect

count = 0
for i in range(1, n + 1): # Iterate prefix sums
    target = prefix_sum[i] - x
    if target < 0:
        continue
    # Find first position in prefix_sum greater than target
    pos = bisect.bisect_right(prefix_sum, target, 0, i)
    count += pos # 0 ~ pos-1 all satisfy condition, directly count pos
    
print(count)
