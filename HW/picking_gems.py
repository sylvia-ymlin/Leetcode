# Given a set of numbers, select x numbers such that their product is not less than y
# Output number of ways

# Array length less than 20
# Brute force enumeration

from itertools import combinations
n, x, y = map(int, input().split())
arr = list(map(int, input().split()))
count = 0
for combo in combinations(arr, x): # Why not permutations? Because order doesn't matter for product.
    prod = 1
    for num in combo:
        prod *= num
    if prod >= y:
        count += 1

print(count)