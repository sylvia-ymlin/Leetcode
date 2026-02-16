# Search if word exists
# Add current letter to path
# Recursively process next letter
# Undo choice

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # Decision set
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        # (x,y) current position
        # index current letter index
        def backtrack(x, y, index = 0):
            
            if board[x][y] != word[index]:  # Current letter mismatch
                return False
            
            # If all letters matched
            if index == len(word) - 1:
                return True
            
            # Recursively process next letter
            visited.add((x, y))  # Mark current position as visited
            exist = False
            for dx, dy in directions:  # Four directions
                # Input check
                nx, ny = x + dx, y + dy  # New position
                if 0 <= nx < len(board) and 0 <= ny < len(board[0]) and (nx, ny) not in visited:
                    if backtrack(nx, ny, index + 1):  # Recursively process next letter
                        exist = True
                        break
                
            visited.remove((x, y))  # Undo choice
            return exist
        
        # Do not visit visited points again
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j):
                    return True  # Found matching path
                
        return False  # All starting points failed to find matching path

# Time complexity: O(M * N * 3^L), where M and N are rows and cols of matrix, L is word length. 3 because from a -> b, visited path not visited again, only 3 directions to explore.
# Space complexity: O(max(MN, L)), MN is size of visited set, L is recursion stack depth.