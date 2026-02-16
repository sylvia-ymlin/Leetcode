# A row of n poplar trees, m trees died, can replant k trees
# Calculate max length of continuous survived poplar trees after replanting

n = int(input())
m = int(input())
dead_lists = set(map(int, input().split()))
k = int(input())

# This is a sliding window problem
# When count of dead trees in window <= k, extend right boundary
# When count > k, shrink left boundary until condition met. Calculate current window length, update max.

left = right = 1 # Tree indices start from 1
max_len = 0
dead_count = 0
while right <= n:
    if right in dead_lists:
        dead_count += 1
    while dead_count > k:
        if left in dead_lists:
            dead_count -= 1
        left += 1
    max_len = max(max_len, right - left + 1)
    right += 1
print(max_len)