# Draw rectangles
# Give operation and diagonal coordinates representing a rectangle
# Operation d means draw, e means erase
# Calculate area of final shape

# Convert all rectangles to (1x1) small grids, calculate drawn area

# Known range [-100, 100]
grid = [[0]*201 for _ in range(201)]

n = int(input())


for _ in range(n):
    line = input().strip().split()
    op = line[0]
    x1, y1, x2, y2 = map(int, line[1:])
    # Coordinates to array indices
    x1 += 100
    y1 += 100
    x2 += 100
    y2 += 100
    val = 1 if op == 'd' else 0
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = val
# Calculate area
area = sum(sum(row) for row in grid)
print(area)
