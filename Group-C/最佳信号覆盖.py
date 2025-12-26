# 一组 AP
# 需要找到信号最好的一处坐标，有多处，取最小的坐标

# 给出每个 ap 信号覆盖的坐标
# 求并集
# 遍历，求每处坐标的信号强度，取最大值

# 信号强度 s//(1+d), 向下取整，所以直接用整除 //

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


# 计算每个坐标的信号强度
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