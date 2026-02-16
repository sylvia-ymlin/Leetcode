# Find subarray from a set of numbers, such that array sum is divisible by m
# Found output 1, not found output 0

'''
    Sliding window solves magnitude problem,
    Prefix sum solves relationship problem -> modulo, difference, sum
'''
# Non-monotonic relationship, use prefix sum
# Find two prefix sums whose difference is divisible by m

# Input n and m
n, m = map(int, input().split())
# Input array
arr = list(map(int, input().split()))

# Calculate prefix sum, and record remainder of each prefix sum mod m
# Because only need to determine existence, only need to record if remainder has appeared <- Important!!!

mod = set()
prefix_sums = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sums[i] = (prefix_sums[i - 1] + arr[i - 1])
    if prefix_sums[i] % m in mod:
        print(1)
        exit(0)
    mod.add(prefix_sums[i] % m)

print(0)