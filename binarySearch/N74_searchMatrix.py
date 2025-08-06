# 矩阵，按行递增，二维查找
# 数组元素 i, 在矩阵中位置 [i // n][i % n]

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_x = mid // len(matrix[0])
            mid_y = mid % len(matrix[0])
            mid_val = matrix[mid_x][mid_y]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False