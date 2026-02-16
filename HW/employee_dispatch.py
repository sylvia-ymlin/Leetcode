# Input
# a b c d
# a: Code for country x
# b: Code for country y
# c: Number of people dispatched to country x
# d: Number of people dispatched to country y

# IDs are shared. Dispatch rules:
# IDs that are multiples of a cannot go to country x
# IDs that are multiples of b cannot go to country y
# Output minimum k such that IDs in [1, k] satisfy requirements

# Read input
a, b, c, d = map(int, input().split())

# For a given k, determine number of people that can be dispatched, then binary search k
# Define sequence interval according to problem requirements
left, right = 1, 10**9
while left < right:
    k = (left + right) // 2

    # X needs how many more? Count is number of IDs explicitly assignable to X
    need_x = max(0, c - (k // b - k // (a*b)))
    # Y needs how many more? Count is number of IDs explicitly assignable to Y
    need_y = max(0, d - (k // a - k // (a*b)))

    # Number of assignable but unassigned IDs
    total_available = k - k // a - k // b + k // (a*b)

    if total_available >= need_x + need_y:
        right = k
    else:
        left = k + 1

print(left)