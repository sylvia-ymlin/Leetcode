# A group of APs (Access Points)
# Find coordinate with best signal. If multiple, pick smallest coordinate

# Given coordinates covered by each AP
# Find union? No, intersection?
# Traverse, calculate signal strength at each coordinate, pick max

# Signal strength s // (1 + d), floor division, so use // directy

n, max_dist = map(int, input().split())
ap_ranges = []
for _ in range(n):
    x, y, s = map(int, input().split())
    ap_ranges.append((x, y, s))

singal_coords = dict() # key: coord, value: AP index list
for i, (x, y, s) in enumerate(ap_ranges):
    for coord_x in range(x-s, x+s+1):
        for coord_y in range(y-s, y+s+1):
            singal_coords[(coord_x, coord_y)] = singal_coords.get((coord_x, coord_y), []) + [i]


# Calculate signal strength for each coordinate
max_singal = -1
best_coord = None
for coord, ap_idx_list in singal_coords.items():
    total_singal = 0
    for ap_idx in ap_idx_list:
        x, y, s = ap_ranges[ap_idx]
        dist = max(abs(coord[0]-x), abs(coord[1]-y))
        total_singal += s // (1 + dist)
    if total_singal > max_singal and coord[0] >= 0 and coord[1] >= 0:
        max_singal = total_singal
        best_coord = coord

print(best_coord[0], best_coord[1])