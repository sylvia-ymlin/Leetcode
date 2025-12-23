from typing import List

# 图中连通分量的个数

# 深度优先搜索
# 搜索到一个结点，访问所有与之连通的结点
# 访问图中其他未访问结点
# 基于递归实现
class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 将二维网格视为无向图，相邻的1代表连通
        # 遍历网格，遇到1就进行DFS，将与之连通的1都标记为0
        # 如果可以修改原数组，就直接在原数组上操作
        # 如果不可以，就需要额外的visited数组 -> 增加空间复杂度O(MN)
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(r, c):
            # 越界或遇到0就返回
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # 图内遇到 1，标记为访问过‘0’
            grid[r][c] = '0'
            # 访问上下左右四个方向
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
    
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # 遇到岛屿
                    num_islands += 1  # 岛屿数量加1
                    dfs(r, c)         # 进行DFS，标记与之连通的岛屿为0
        
        return num_islands

# 广度优先搜索：
# 访问一个结点，访问所有与之直接连通的结点
# 然后依次访问这些结点的连通结点
# 直到没有新的结点可访问
# 基于队列实现
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0 # 存储结构，决定了是空
        
        nc = len(grid[0])
        num_islands = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1': # 遇到岛屿
                    num_islands += 1  # 岛屿数量加1
                    grid[r][c] = '0'  # 标记为访问过
                    # 广度优先搜索
                    queue = [(r, c)]
                    while queue:
                        row, col = queue.pop(0) # 出队列
                        # 访问上下左右四个方向
                        directions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
                        for dr, dc in directions:
                            if 0 <= dr < nr and 0 <= dc < nc and grid[dr][dc] == '1':
                                grid[dr][dc] = '0' # 标记为访问过
                                queue.append((dr, dc)) # 入队列
        return num_islands

# 并查集
# 并查集个数就是连通分量的个数
class Solution3:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        
        nc = len(grid[0])
        uf = UnionFind(grid) # 初始化并查集
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    # 访问上下左右四个方向的点的位置
                    directions = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                    for dr, dc in directions:
                        if 0 <= dr < nr and 0 <= dc < nc and grid[dr][dc] == '1':
                            # 找到与当前点连通的点，合并集合
                            uf.union(r * nc + c, dr * nc + dc) # 合并集合
        return uf.count

class UnionFind:
    def __init__(self, grid): # 定义了初始化的逻辑
        m, n = len(grid), len(grid[0])
        self.count = 0  # 岛屿数量（独立组的数量）
        self.parent = [-1] * (m * n)  # 父节点数组
        self.rank = [0] * (m * n)     # 树的高度，用于优化
        
        # 初始化：每个'1'都是独立的岛屿；水域-1，不参与
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    # 二维坐标转一维索引：(i,j) -> i*n + j
                    index = i * n + j
                    self.parent[index] = index  # 自己是自己的父节点
                    self.count += 1  # 岛屿数量+1
    
    def find(self, i):
        """
        查找元素i的根节点（代表元素）
        路径压缩：让路径上所有节点直接指向根节点，压缩当前结点所在路径
        """
        if self.parent[i] != i:
            # 递归查找并压缩路径，递归直到某个节点值 == index
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        """
        合并x和y所在的两个集合
        """
        rootx = self.find(x)  # 找到x的根节点
        rooty = self.find(y)  # 找到y的根节点
        
        # 根节点不同，不在一个集合
        if rootx != rooty:
            # 按秩合并：将小树挂到大树下面
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx  # 交换，确保rootx更高
            
            self.parent[rooty] = rootx  # 将rooty的根设为rootx
            
            # 如果两树高度相同，合并后高度+1
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            # 挂到根节点的小树，不影响大树的高度
            
            self.count -= 1  # 集合数量减1
    
    def getCount(self):
        """返回独立集合的数量（岛屿数量）"""
        return self.count

