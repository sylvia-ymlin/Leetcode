# 搜索单词是否存在
# 当前字母加入路径
# 递归处理下一个字母
# 撤销选择

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # 决策集合
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 右，下，左，上

        # (x,y) 当前位置
        # index 当前处理的字母索引
        def backtrack(x, y, index = 0):
            
            if board[x][y] != word[index]:  # 当前字母不匹配
                return False
            
            # 如果已经匹配完所有字母
            if index == len(word) - 1:
                return True
            
            # 递归处理下一个字母
            visited.add((x, y))  # 标记当前位置已访问
            exist = False
            for dx, dy in directions:  # 四个方向
                # 输入判断
                nx, ny = x + dx, y + dy  # 新位置
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx, ny) not in visited:
                    if backtrack(nx, ny, index + 1):  # 递归处理下一个字母
                        exist = True
                        break
                
            visited.remove((x, y))  # 撤销选择
            return exist
        
        # 遍历过的点不再访问
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j):
                    return True  # 找到匹配路径
                
        return False  # 所有起点都没找到匹配的路径

# 时间复杂度： O(M * N * 3^L)，其中 M 和 N 分别是矩阵的行数和列数，L 是单词长度。3 是因为从 a -> b，探寻过的路径不再访问， 只有 3 个方向可以继续探索。
# 空间复杂度： O(max(MN, L)), MN 是 visited 集合的大小，L 是递归栈的深度。