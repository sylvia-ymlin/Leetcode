# transfer the matrix, 顺时针 90 度
# 本地旋转
# this is a math problem, we need to find the rule, that how the position of the roated number placed

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 1 2 3                  7 8 9                   7 4 1
        # 4 5 6 -> 上下对称翻转 -> 4 5 6  -> 主对称轴翻转 -> 8 5 3
        # 7 8 9                  1 2 3                   9 6 3

        n = len(matrix)

        # 上下（水平）翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        
        # 主对称轴翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
# 时间复杂度： O(N^2)，一次翻转移动一半元素
# 空间复杂度：O(1)，原地翻转

# 基于元素翻转后的位置
# for m[i][j], it should be put at m[j][n - 1 - i]
# the problem is, if we directly put the element in its correct place, the original element will be 覆盖

# and we don;t have an simple swap rule
# put m[j][n - 1 - i] = m[i][j]
# put m[n-1-i][n-1-j] = m[j][n - 1 - i]
# put m[n-1-j][i]= m[n-1-i][n-1-j]
# put m[i][j] = m[n-1-j][i]
# so we have need four steps to put four elements into the correct place
# then we take temp = m[n-1-j][i]
# and then m[n-1-j][i]= m[n-1-i][n-1-j], m[n-1-i][n-1-j] = m[j][n - 1 - i], m[j][n - 1 - i] = m[i][j], m[i][j] = temp

# we still need to determin we need to do such swap on which rows and columns
# we splite the matrix to four submatrix

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            for j in range((n+1)//2):
                temp = matrix[n-1-j][i]
                matrix[n-1-j][i]= matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = temp
