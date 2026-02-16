from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # the key point is to find the column and row for the zero element before setting them to zero
        rows, cols = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        
        # set zeros
        for r in range(rows):
            for c in range(cols):
                if r in zero_rows or c in zero_cols:
                    matrix[r][c] = 0

# time complexity is O(M * N), where M is the number of rows and N is the number of columns
# space complexity is O(M + N) for the sets used to track zero rows and columns

# Space optimized version
# time complexity: O(M * N)
# no extra space, space complexity: O(1)
class SolutionOptimized:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # the idea is to use the first row and first column to mark which rows and columns need to be set to zero; and we use a boolean variable to track if the first row needs to be set to zero (for the first column, since we don't modify the first row, it will not affect the first column)
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  # mark the column
                    if r > 0: # not the first row
                        matrix[r][0] = 0 # mark the row
                    else:
                        rowZero = True  # mark the first row

        # set the inner elements to zero
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # set the first column to zero if needed
        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0

        # set the first row to zero if needed
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0