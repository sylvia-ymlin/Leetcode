# 顺时针螺旋顺序返回矩阵中元素

# the most straightforward method is recursively traverse the matrix
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = []

        # row is the number of rows the current submatrix has
        # col is the number of columns the current suabmatrix has
        # r, c are the starting row and column indices of the current submatrix
        # dr, dc are the direction of movement in the row and column respectively
        # that for top row, [0, 1]; -> [dr, dc] -> [dr, dc]
        # for right column, [1, 0];
        # for bottom row, [0, -1];
        # for left column, [-1, 0]
        # row: current traverse, after, -1
        # col: next traverse, after -1
        def dfs(row, col, r, c, dr, dc):
            # when the submatrix has no rows or columns, we stop
            if row == 0 or col == 0:
                return
            
            # we move along the 'column'
            for i in range(col):
                r += dr # how to move in the row direction
                c += dc # how to move in the column direction
                # we append the current element to the result
                res.append(matrix[r][c])
            
            # subproblem, 'transfer' the matrix
            # row - 1, which we just traversed, and exchange column and row
            # dc and dr are swapped and chose the opposite direction for column
            dfs(col, row - 1, r, c, dc, -dr)
        
        dfs(m, n, 0, -1, 0, 1)

        return res