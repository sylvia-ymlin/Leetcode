from typing import List

# Number of connected components in grid

# Depth First Search
# Search a node, visit all connected nodes of it
# Visit other unvisited nodes in graph
# Implemented based on recursion
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Treat 2D grid as undirected graph, adjacent 1s represent connection
        # Traverse grid, if 1 is met, perform DFS, mark all connected 1s as 0
        # If original array can be modified, operate directly on it
        # If not, need extra visited array -> increase space complexity O(MN)
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(r, c):
            # Return if out of bounds or meets 0
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # Meet 1 in graph, mark as visited '0'
            grid[r][c] = '0'
            # Visit four directions: up, down, left, right
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # Meet island
                    num_islands += 1  # Island count +1
                    dfs(r, c)         # Perform DFS, mark connected islands as 0
        
        return num_islands

# Breadth First Search:
# Visit a node, visit all directly connected nodes
# Then visit connected nodes of these nodes in order
# Until no new node can be visited
# Implemented based on queue
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0 # Storage structure determines it's empty
        
        nc = len(grid[0])
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1': # Meet island
                    num_islands += 1  # Island count +1
                    grid[r][c] = '0'  # Mark as visited
                    # Breadth First Search
                    queue = [(r, c)]
                    while queue:
                        row, col = queue.pop(0) # Dequeue
                        # Visit four directions: up, down, left, right
                        directions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
                        for dr, dc in directions:
                            if 0 <= dr < nr and 0 <= dc < nc and grid[dr][dc] == '1':
                                grid[dr][dc] = '0' # Mark as visited
                                queue.append((dr, dc)) # Enqueue
        return num_islands

# Union Find
# Number of union find sets is number of connected components
class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        
        nc = len(grid[0])
        uf = UnionFind(grid) # Initialize UnionFind
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    # Visit positions of points in four directions (up, down, left, right)
                    directions = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                    for dr, dc in directions:
                        if 0 <= dr < nr and 0 <= dc < nc and grid[dr][dc] == '1':
                            # Find connected point, merge sets
                            uf.union(r * nc + c, dr * nc + dc) # Merge sets
        return uf.count

class UnionFind:
    def __init__(self, grid): # Define initialization logic
        m, n = len(grid), len(grid[0])
        self.count = 0  # Number of islands (independent groups)
        self.parent = [-1] * (m * n)  # Parent node array
        self.rank = [0] * (m * n)     # Tree height, for optimization
        
        # Initialization: each '1' is an independent island; water -1, not participating
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # 2D coordinate to 1D index: (i,j) -> i*n + j
                    index = i * n + j
                    self.parent[index] = index  # Self is parent
                    self.count += 1  # Island count +1
    
    def find(self, i):
        """
        Find root node (representative element) of element i
        Path compression: make all nodes on path point directly to root, compress path of current node
        """
        if self.parent[i] != i:
            # Recursively find and compress path, recurse until node value == index
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        """
        Merge two sets containing x and y
        """
        rootx = self.find(x)  # Find root of x
        rooty = self.find(y)  # Find root of y
        
        # Roots are different, not in same set
        if rootx != rooty:
            # Union by rank: hang smaller tree under larger tree
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx  # Swap, ensure rootx is higher
            
            self.parent[rooty] = rootx  # Set root of rooty to rootx
            
            # If heights are same, height +1 after merge
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            # Small tree hanging to root, doesn't affect large tree height
            
            self.count -= 1  # Set count -1
    
    def getCount(self):
        """Return number of independent sets (island count)"""
        return self.count

