# A and B divide apples into two piles

# Output: Number of apples, weight of each apple
n = int(input())
weights = list(map(int, input().split()))

# Output: Total weight of apples B gets
# A requires calculating total weight of apples in binary and then dividing equally. Calculation rule: convert to binary, no carry
# B calculates weight in normal decimal
# Require maximizing weight B gets while satisfying A's requirement

# No-carry binary equals bitwise XOR
# Calculate XOR sum of total weights. If 0, it means can be divided equally, then take the smallest apple for A, rest for B
# Cannot satisfy A's requirement -> Cannot divide equally, return -1

total_xor = 0
total_sum = 0
for w in weights:
    total_xor ^= w # Calculate XOR value
    total_sum += w

if total_xor != 0:
    print(-1)
else:
    min_weight = min(weights)
    b_weight = total_sum - min_weight
    print(b_weight)