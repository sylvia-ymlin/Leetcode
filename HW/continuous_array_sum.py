# Find number of continuous subarrays with sum greater than x

# Continuous subarray, and elements are all positive numbers
# Prefix sum, if one prefix sum is greater than x, then all subsequent prefix sums are greater than x? No, this logic is slightly wrong but let's see code.
# Code uses sliding window? Or two pointers.

n, x = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

count = 0
right = 0
for left in range(n):
    # Find minimum right endpoint where sum starting from left is >= x
    while right < n and prefix_sum[right + 1] - prefix_sum[left] < x:
        right += 1
    # Number of subarrays starting with [left, right]
    count += n - right

print(count)