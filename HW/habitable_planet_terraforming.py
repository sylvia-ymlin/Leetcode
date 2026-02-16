# Rotten Oranges variant
# In an m * n grid, there are cells with Yes, No, and Na states
# Each time step, Yes spreads to adjacent No cells (up, down, left, right)
# Na cells cannot be spread to
# Calculate how many time steps until all spreadable No cells become Yes
# If there are No cells that cannot be spread to, return -1

# Read matrix
from collections import deque
import sys
# Read data
# Input format: Directly an m rows n columns matrix, elements are YES, NO, NA
# TRUE FALSE TRUE
# FALSE NA FALSE

grid = []

try:
    while True:
        line = input().strip()
        if not line:  # Empty line indicates end
            break
        grid.append(line.split())
except EOFError:  # EOF indicates end
    pass

if not grid:
    print(-1)
    sys.exit()

m, n = len(grid), len(grid[0])

count = 0 # Record number of No cells
# Init queue, store all initial Yes positions
queue = deque()
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'YES':
            queue.append((i, j))
        elif grid[i][j] == 'NO':
            count += 1

# Direction vectors, representing up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


time_steps = 0
# BFS spreading process
while queue and count > 0:
    time_steps += 1
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Check boundaries and state
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 'NO': 
                grid[nx][ny] = 'YES'  # Spread
                count -= 1
                queue.append((nx, ny))

# Output result
if count == 0:
    print(time_steps)
else:
    print(-1)
