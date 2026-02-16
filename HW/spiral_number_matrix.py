# Fill m rows matrix with numbers 1 to n
# Minimize columns -> m x (ceil(n/m)) matrix
# Fill insufficient parts with 0? Wait, sample says '*'. 
# Original comment: "Digits insufficient fill with 0". But code fills '*'.
# "Writing method: Clockwise spiral"

# Read input
n, m = map(int, input().split())

rows = m
cols = n // m + (1 if n % m != 0 else 0)

# Initialize matrix, 0 means unvisited
matrix = [[0] * cols for _ in range(rows)]

# Spiral fill
num = 1
# Directions: Right, Down, Left, Up
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0  # Current direction index
row, col = 0, 0  # Current position

while num <= rows * cols:
    if num <= n:
        matrix[row][col] = num
    else:
        matrix[row][col] = '*' # Fill empty with '*'
    num += 1

    # Calculate next position
    next_row = row + directions[dir_idx][0]
    next_col = col + directions[dir_idx][1]

    # Check boundaries and if visited
    if (0 <= next_row < rows and 0 <= next_col < cols and matrix[next_row][next_col] == 0):
        row, col = next_row, next_col
    else: # Blocked, change direction
        dir_idx = (dir_idx + 1) % 4
        row += directions[dir_idx][0]
        col += directions[dir_idx][1]
    

# Output (transpose? No, simply print rows)
for row in matrix:
    print(' '.join(str(x) for x in row))
