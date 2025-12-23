# 第 i 个棋子有 n - i 个位置可以放置
# 回溯
# 从 i 开始 尝试放置
# i == n, 得到一个解
# 回溯到 i - 1，尝试下一个位置

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        columns = set()  # 列
        diag1 = set()    # 主对角线
        diag2 = set()    # 副对角线

        # 棋子编号和行映射，只记录放置的列
        # 主对角线编号 i - j
        # 副对角线编号 i + j


        # 按 列 放置
        def backtrack(i=0, path=[]):
            if i == n:  # 放置完所有棋子
                res.append(path[:])
                return
            
            for j in range(n):  # 尝试放置在第 j 列
                if j in columns or (i - j) in diag1 or (i + j) in diag2:
                    continue
                # 放置棋子
                columns.add(j)
                diag1.add(i - j)
                diag2.add(i + j)
                path.append(j)  # 记录放置位置
                backtrack(i + 1, path)

                # 回溯，撤销放置
                columns.remove(j)
                diag1.remove(i - j)
                diag2.remove(i + j)
                path.pop()
        
        backtrack()
        # 将结果转换为棋盘字符串格式
        return [["." * j + "Q" + "." * (n - j - 1) for j in path] for path in res]  

# 时间复杂度： O(N!)，每个棋子有 N 个位置可以放置，最多放置 N 个棋子
# 空间复杂度： O(N)，存储棋子放置位置的路径

# 使用位运算记录皇后的信息
class SolutionBit:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def backtrack(i=0, path=[], columns=0, diag1=0, diag2=0):
            if i == n:  # 放置完所有棋子
                res.append(path[:])
                return
            
            for j in range(n):
                # 检查列和对角线是否被占用
                if (columns & (1 << j)) or (diag1 & (1 << (i - j + n - 1))) or (diag2 & (1 << (i + j))):
                    continue
                
                # 放置棋子
                columns |= (1 << j)
                diag1 |= (1 << (i - j + n - 1))
                diag2 |= (1 << (i + j))
                path.append(j)  # 记录放置位置
                backtrack(i + 1, path, columns, diag1, diag2)

                # 回溯，撤销放置
                columns &= ~(1 << j)
                diag1 &= ~(1 << (i - j + n - 1))
                diag2 &= ~(1 << (i + j))
                path.pop()
        
        res = []
        backtrack()
        return [["." * j + "Q" + "." * (n - j - 1) for j in path] for path in res]