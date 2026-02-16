# Input, first line is length, width of survey area, side length of station to be built (square), minimum power requirement
# Power generation of each area
# For example, a 2 x 5 area
# Given a 2-row 5-column matrix, representing power generation of each cell

# Output: Number of stations meeting power requirement

length, width, station_size, mini_power = map(int, input().strip().split())
matrix = [list(map(int, input().strip().split())) for _ in range(length)]

# Brute force enumeration of all possible station positions, since area size is fixed
res = 0
for i in range(length - station_size + 1):
    for j in range(width - station_size + 1):
        power = 0
        for x in range(i, i + station_size):
            for y in range(j, j + station_size):
                power += matrix[x][y]
        if power >= mini_power:
            res += 1
print(res)

# Time complexity O(L * W * S^2) -> because need to traverse S^2 cells to calculate power in an area

# Can use prefix sum to optimize area power calculation
# 2D prefix sum
prefix_sum = [[0] * (width + 1) for _ in range(length + 1)]
# prefix_sum[i,j] represents sum of area from (0,0) to (i-1,j-1)
for i in range(1, length + 1):
    for j in range(1, width + 1):
        prefix_sum[i][j] = matrix[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

res = 0
for i in range(length - station_size + 1):
    for j in range(width - station_size + 1):
        x1, y1 = i, j
        x2, y2 = i + station_size, j + station_size
        power = prefix_sum[x2][y2] - prefix_sum[x1][y2] - prefix_sum[x2][y1] + prefix_sum[x1][y1]
        if power >= mini_power:
            res += 1
print(res)