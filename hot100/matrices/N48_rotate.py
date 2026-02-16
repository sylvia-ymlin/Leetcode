# Rotate the matrix, 90 degrees clockwise
# Rotate in-place
# This is a math problem, we need to find the rule, that how the position of the rotated number placed

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # 1 2 3                  7 8 9                   7 4 1
        # 4 5 6 -> Flip upside down ->  4 5 6  -> Flip along main diagonal -> 8 5 3
        # 7 8 9                  1 2 3                   9 6 3

        n = len(matrix)

        # Flip upside down (horizontally)
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        
        # Flip along main diagonal
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
# Time Complexity: O(N^2), one flip moves half of elements
# Space Complexity: O(1), in-place flip

# Based on position after element rotation
# for m[i][j], it should be put at m[j][n - 1 - i]
# the problem is, if we directly put the element in its correct place, the original element will be overwritten

# and we don't have a simple swap rule
# put m[j][n - 1 - i] = m[i][j]
# put m[n-1-i][n-1-j] = m[j][n - 1 - i]
# put m[n-1-j][i]= m[n-1-i][n-1-j]
# put m[i][j] = m[n-1-j][i]
# so we have need four steps to put four elements into the correct place
# then we take temp = m[n-1-j][i]
# and then m[n-1-j][i]= m[n-1-i][n-1-j], m[n-1-i][n-1-j] = m[j][n - 1 - i], m[j][n - 1 - i] = m[i][j], m[i][j] = temp

# we still need to determine we need to do such swap on which rows and columns
# we split the matrix to four submatrix

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
