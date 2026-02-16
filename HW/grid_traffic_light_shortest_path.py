# Given a grid, grid elements can be 0 (empty), 1 (obstacle), 2 (traffic light)
# Moving one cell takes 1 second
# Encountering a traffic light requires waiting. (2, 2, 3) means wait time at coordinate (2,2) is 3 seconds

# Output shortest time from (0,0) to (m-1,n-1)

# Due to obstacles, movement is not just right and down, can also be up and left
# This problem is essentially a shortest path problem in a weighted graph
# Dijkstra algorithm is suitable

# Read input
# Read 2D array first, given as a list
# [[0, 1, 0], [0, 2, 1], [0, 0, 0]]
matrix = eval(input())

if matrix[0][0] == 1 or matrix[-1][-1] == 1:
    print(-1)
    exit()

n, m = len(matrix), len(matrix[0])
# Construct wait time matrix
wait_time = [[0] * m for _ in range(n)]

# Read traffic light info, also given as a 2D array
wait_time_info = eval(input())
# Fill wait time matrix
for x, y, w in wait_time_info:
    wait_time[x][y] = w

# Dijkstra algorithm
dist = [[float('inf')] * m for _ in range(n)] # Record shortest time from start to each point, init infinity
dist[0][0] = 0

import heapq

heap = [(0, 0, 0)] # (time, x, y)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # Right, Down, Left, Up

while heap:
    cur_time, x, y = heapq.heappop(heap)
    
    # cur_time is the current time reaching (x, y)
    # If greater than known shortest time, skip
    if cur_time > dist[x][y]:
        continue
    
    # Found a better path, try updating neighbors
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        # Check if reachable
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] != 1:
            next_time = cur_time + 1 + wait_time[nx][ny]
            # Update shortest time for neighbor
            if next_time < dist[nx][ny]:
                dist[nx][ny] = next_time
                heapq.heappush(heap, (next_time, nx, ny))

print(dist[-1][-1] if dist[-1][-1] != float('inf') else -1)
