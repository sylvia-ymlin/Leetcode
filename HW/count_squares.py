# Input n 2D coordinates, find number of squares formed
# Output number of squares

# Problem gives coordinate range
# All points do not coincide, so no duplicate points
# Coordinate range -10, 10
# Enumerate all points, use this point as top-left, check if bottom-right point exists, then check if other two points exist
# Enumerate all points, use this point as left vertex, enumerate right vertex, check if top/bottom two points exist
# No, there are many ways to form a square, still use vectors to judge

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

count = 0
if n < 4:
    print(0)
    exit(0)

# Pairwise traverse all points, assume these two points are diagonal of a square, check if other two points exist
# For each pair of points (x1, y1), (x2, y2)
# The other two points forming the square are
# Find midpoint, rotate half-diagonal vector by 90 degrees
# Midpoint (mx, my) = ((x1 + x2) / 2, (y1 + y2) / 2)
# Half-diagonal vector (dx, dy) = ((x2 - x1) / 2, (y2 - y1) / 2)
# Two points after 90 degree rotation
# Point 3: (mx - dy, my + dx)
# Point 4: (mx + dy, my - dx)

for i in range(n):
    x1, y1 = points[i]
    for j in range(i + 1, n):
        x2, y2 = points[j]
        mx = (x1 + x2) / 2
        my = (y1 + y2) / 2
        dx = (x2 - x1) / 2
        dy = (y2 - y1) / 2
        x3, y3 = mx - dy, my + dx
        x4, y4 = mx + dy, my - dx
        if (x3, y3) in points and (x4, y4) in points:
            count += 1

# Each square is counted twice because each square has two diagonals
print(count // 2)
