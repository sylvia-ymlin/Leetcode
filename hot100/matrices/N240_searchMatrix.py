# Matrix elements are sorted, search for target element
# Sorted ascending from left to right
# Sorted ascending from top to bottom

# Traverse by main diagonal elements
import bisect
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])

        def binary_search(row, target):
            left, right = 0, len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        
        # Binary search, stored by row, considering efficiency, search by row
        for row in matrix:
            if binary_search(row, target):  # Return True/False directly
                return True
        return False  # Not found in any row

matrix = [[-5]]
sol = Solution()
res = sol.searchMatrix(matrix, -5)

print(res)

# Search in Z-shape starting from top right corner, equal returns true
# Only two movement directions:
# Smaller than target: move down
# Larger than target: move left
class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False
