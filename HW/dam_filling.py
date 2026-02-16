# A dam breaks, use a batch of wood to fill the gap
# Find the solution that maximizes filled area with minimum number of wood used
# Each gap can only be filled by one piece of wood

n = int(input().strip()) # Length of dam gap array
# Dam gap array
damages = list(map(int, input().strip().split(',')))
# Wood array length
m = int(input().strip())
# Wood array
woods = list(map(int, input().strip().split(',')))

# Calculate gap depth
base_h = damages[0]
gaps = []
for i in range(1, n-1):
    gaps.append(base_h - damages[i])

# Sort gap area and wood height
gaps.sort(reverse=True) # Gap area from large to small
woods.sort() # Wood height from small to large

usde = [False] * m
total_height = 0

# Greedy matching
# Prioritize finding shortest wood that can fill, if not found, find longest wood
for gap in gaps:
    best_fit = -1
    for j in range(m):
        if not usde[j] and woods[j] >= gap:
            best_fit = j
            break
    if best_fit == -1:
        for j in range(m-1, -1, -1):
            if not usde[j]:
                best_fit = j
                break
    
    # Unless no wood left, must find one
    if best_fit == -1:
        break

    usde[best_fit] = True
    total_height += woods[best_fit]

print(total_height)