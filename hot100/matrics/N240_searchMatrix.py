# 矩阵中元素有序，查找目标元素
# 从左到右升序
# 从上到下升序

# 按主对角元素遍历
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
        
        # 二分查找, 按行存储，考虑到效率，按行查找
        for row in matrix:
            if binary_search(row, target):  # 直接返回True/False
                return True
        return False  # 所有行都没找到

matrix = [[-5]]
sol = Solution()
res = sol.searchMatrix(matrix, -5)

print(res)

# 从 右上角开始 z 字型搜索， 等于，返回 true
# 只有两个移动方向：
# 小于目标值：向下移动
# 大于目标值：向左移动
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
