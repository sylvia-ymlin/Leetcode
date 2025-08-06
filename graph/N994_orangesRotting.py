# 腐烂的橘子会导致相邻的橘子也腐烂
# 需要返回腐烂所有橘子所需的分钟数

# 暴力解法：给每个新鲜橙子初始化腐烂时间 为 inf
# 维护一个全局的最小分钟数 inf
# 枚举每个腐烂的橘子，向四个方向扩散，对相邻的新鲜橘子更新腐烂时间， min(当前时间+1, 新鲜橘子腐烂时间), 更新全局最小分钟数 min（全局最小分钟数, 当前时间+1）

# 最后检查是否有新鲜橘子未腐烂
# 如果有，返回 -1，否则返回全局最小分钟数
# 这种枚举方式时间复杂度 O(MN * (M+N))，空间复杂度 O(MN)，耗时较长

# 广度优先搜索
# 所有的腐烂橘子在广度优先搜索上都是同一层
# 所以我们第一次遍历，将所有腐烂橘子入队
# 然后开始 BFS，遍历每个腐烂橘子，向四个方向扩散
# 如果相邻的新鲜橘子被腐烂，更新其腐烂时间，并入队
# 每次 BFS 扩散完一层，分钟数加1
# 当队列为空时，说明所有腐烂橘子都被处理完
# 最后检查是否有新鲜橘子未腐烂
# 如果有，返回 -1，否则返回分钟数

from typing import List
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 初始化队列
        queue = collections.deque()

        rows, cols = len(grid), len(grid[0])

        # 第一次遍历，将所有腐烂橘子入队
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:  # 腐烂的橘子
                    queue.append((r, c, 0)) # (行, 列, 当前分钟数)
                    # 我们需要标记节点被腐烂时间

        def neighbors(r, c):
            # 返回四个方向的相邻坐标
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

        minutes = 0
        # 广度优先搜索
        while queue:
            r, c, minutes = queue.popleft()  # 出队列，获取当前橘子位置和分钟数
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == 1:  # 新鲜橘子
                    grid[nr][nc] = 2  # 标记为腐烂
                    queue.append((nr, nc, minutes + 1))  # 入队列，分钟数加1
        
        # 收尾检查
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  # 如果还有新鲜橘子未腐烂
                    return -1
                
        return minutes  # 返回总分钟数

            
        