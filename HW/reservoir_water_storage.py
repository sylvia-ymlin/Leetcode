# Trapping Rain Water variant, only one storage interval allowed, find max storage volume and interval
# Idea: First solve Trapping Rain Water, calculate max height reachable after storing water at each position

# Read data as list of int
height = list(map(int, input().split()))
n = len(height)

if n < 3:
    print(0)
    exit()

# 1. Preprocess left and right max
left_max = [0] * n
right_max = [0] * n

for i in range(1, n):
    left_max[i] = max(left_max[i-1], height[i-1])

for i in range(n-2, -1, -1):
    right_max[i] = max(right_max[i+1], height[i+1])

# 2. Calculate storage amount at each position
water = [max(0, min(left_max[i], right_max[i]) - height[i]) for i in range(n)]

# 3. Find max volume of continuous storage block
best = 0
ans_l = ans_r = 0
i = 0

while i < n:
    if water[i] == 0:
        i += 1
        continue

    left = i
    current_volume = 0
    while i < n and water[i] > 0:
        current_volume += water[i]
        i += 1
    right = i - 1

    if current_volume > best or (current_volume == best and right - left < ans_r - ans_l):
        best = current_volume
        ans_l = left
        ans_r = right

# left and right record ends with water, need to adjust to interval including boundaries for output
if best == 0:
    print(0)
else:
    print(f"{ans_l - 1} {ans_r + 1}:{best}")