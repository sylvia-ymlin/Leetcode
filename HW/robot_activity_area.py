# A m x n grid
# Grid has numbers. A robot can move between adjacent grids. Find max range robot can be active -> Number of reachable grids
# Judging from samples, can robot move in multiple disjoint areas? No.
# Pick the largest area.
# Start from a point, BFS -> Calculate connected component size -> Each point visited once -> O(mn)
# Mark visited points as negative

# Need queue
from collections import deque

m, n = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(m)]


def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    grid[start_x][start_y] *= -1  # Mark as visited
    area_size = 1
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up Down Left Right
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                # For adjacent points, can only move if absolute difference <= 1, then mark visited; because might reach from other paths
                if abs(abs(grid[nx][ny]) - abs(grid[x][y])) <= 1:
                    grid[nx][ny] *= -1  # Mark as visited
                    area_size += 1
                    queue.append((nx, ny))

    return area_size

max_area = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] != -1: # Wait, original logic used > 0 check? No, != -1 check implies not visited?
            # Original code check: if grid[i][j] > 0 used in bfs.
            # But here `if grid[i][j] != -1`.
            # If input has negative numbers? Problem says "digits", usually positive.
            # Assuming input positive.
            if grid[i][j] > 0:
                area_size = bfs(i, j)
                max_area = max(max_area, area_size)

print(max_area)