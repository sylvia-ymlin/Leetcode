# Rotten oranges cause adjacent oranges to rot
# Need to return minutes required for all oranges to rot

# Brute force: Initialize rot time for each fresh orange as inf
# Maintain a global minimum minutes inf
# Enumerate each rotten orange, spread to four directions, update rot time for adjacent fresh oranges, min(current time + 1, fresh orange rot time), update global minimum minutes min(global minimum minutes, current time + 1)

# Finally check if there are fresh oranges not rotten
# If yes, return -1, otherwise return global minimum minutes
# This enumeration time complexity O(MN * (M+N)), space complexity O(MN), takes longer time

# Breadth First Search
# All rotten oranges are on same level in BFS
# So in first traversal, enqueue all rotten oranges
# Then start BFS, traverse each rotten orange, spread to four directions
# If adjacent fresh orange rots, update its rot time, and enqueue
# Each time BFS finishes a layer, minutes + 1
# When queue empty, means all rotten oranges processed
# Finally check if there are fresh oranges not rotten
# If yes, return -1, otherwise return minutes

from typing import List
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initialize queue
        queue = collections.deque()

        rows, cols = len(grid), len(grid[0])

        # First traversal, enqueue all rotten oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:  # Rotten orange
                    queue.append((r, c, 0)) # (row, col, current minutes)
                    # We need to mark node rot time

        def neighbors(r, c):
            # Return adjacent coordinates in four directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

        minutes = 0
        # Breadth First Search
        while queue:
            r, c, minutes = queue.popleft()  # Dequeue, get current orange position and minutes
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:  # Fresh orange
                    grid[nr][nc] = 2  # Mark as rotten
                    queue.append((nr, nc, minutes + 1))  # Enqueue, minutes + 1
        
        # Final check
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  # If fresh orange remains
                    return -1
                
        return minutes  # Return total minutes

            
        