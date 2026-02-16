# Given an array, find the longest continuous subarray such that the average is less than or equal to a given value 'target'.

# Output all subarray indices satisfying the condition
# Format: start_index-end_index

# Essentially finding a continuous interval satisfying a constraint (average <= target), this type of problem is naturally solved using sliding window / two pointers

# Read input
target = int(input())
arr = list(map(int, input().split()))

n = len(arr)

res = []
i = 0

while i < n:
    cur_sum = 0
    length = 0
    start = i

    # Extend to the right
    while i < n and (cur_sum + arr[i]) / (length + 1) <= target:
        cur_sum += arr[i]
        length += 1
        i += 1
    
    # Cannot extend further, record current interval
    if length > 0:
        res.append(f"{start}-{start + length - 1}")
    
    # If entered while loop, length must be > 0, no need to add 1
    if length == 0:
        i += 1


# Output result
if res:
    print(' '.join(res))
else:
    print("NULL")
