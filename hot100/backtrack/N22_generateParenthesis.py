# Generate Parentheses
# Left and correct parentheses must match
# Count number of left and right parentheses
# Number of right parentheses cannot be greater than number of left parentheses

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(left=0, right=0, path=[]):
            # Generated a valid parenthesis combination, add and return
            if left == n and right == n:
                res.append("".join(path)) # Convert list to string
                return
            
            if left < n:  # Can add left parenthesis
                path.append("(")  # Add left parenthesis
                backtrack(left + 1, right, path)
                path.pop()  # Undo choice

            if right < left:  # Can add right parenthesis
                path.append(")")  # Add right parenthesis
                backtrack(left, right + 1, path)
                path.pop()  # Undo choice
        
        backtrack()
        return res