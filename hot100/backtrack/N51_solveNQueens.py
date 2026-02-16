# The i-th piece has n - i positions to be placed
# Backtracking
# Try placing from i
# i == n, get a solution
# Backtrack to i - 1, try next position

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        columns = set()  # Columns
        diag1 = set()    # Main diagonal
        diag2 = set()    # Anti-diagonal

        # Mapping of piece number and row, only record placed column
        # Main diagonal number i - j
        # Anti-diagonal number i + j


        # Place by column
        def backtrack(i=0, path=[]):
            if i == n:  # Placed all pieces
                res.append(path[:])
                return
            
            for j in range(n):  # Try placing in j-th column
                if j in columns or (i - j) in diag1 or (i + j) in diag2:
                    continue
                # Place piece
                columns.add(j)
                diag1.add(i - j)
                diag2.add(i + j)
                path.append(j)  # Record placement position
                backtrack(i + 1, path)

                # Backtrack, undo placement
                columns.remove(j)
                diag1.remove(i - j)
                diag2.remove(i + j)
                path.pop()
        
        backtrack()
        # Convert result to board string format
        return [["." * j + "Q" + "." * (n - j - 1) for j in path] for path in res]  

# Time complexity: O(N!), each piece has N positions to be placed, at most N pieces placed
# Space complexity: O(N), store placement path of pieces

# Use bitwise operation to record queen info
class SolutionBit:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def backtrack(i=0, path=[], columns=0, diag1=0, diag2=0):
            if i == n:  # Placed all pieces
                res.append(path[:])
                return
            
            for j in range(n):
                # Check if column and diagonals are occupied
                if (columns & (1 << j)) or (diag1 & (1 << (i - j + n - 1))) or (diag2 & (1 << (i + j))):
                    continue
                
                # Place piece
                columns |= (1 << j)
                diag1 |= (1 << (i - j + n - 1))
                diag2 |= (1 << (i + j))
                path.append(j)  # Record placement position
                backtrack(i + 1, path, columns, diag1, diag2)

                # Backtrack, undo placement
                columns &= ~(1 << j)
                diag1 &= ~(1 << (i - j + n - 1))
                diag2 &= ~(1 << (i + j))
                path.pop()
        
        res = []
        backtrack()
        return [["." * j + "Q" + "." * (n - j - 1) for j in path] for path in res]