# Partition a substring into palindrome strings
from linecache import cache
from typing import List

# Backtracking + Dynamic Programming
# Backtracking is used to generate all possible partitions
# Dynamic Programming is used to check if a substring is a palindrome

# Find partition
# start: current partition start point
# Substring before [0, start) is already a palindrome, look for partition in [start, end]
# If search reaches end == len(s), partitioning is complete, add current partition result to result set
# Backtrack, remove current partition point, continue searching

# Check if substring is palindrome
# DP array is_palindrome[i][j] indicates whether s[i:j] is a palindrome


class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        is_palindrome = [[True] * n for _ in range(n)]

        # Initialize palindrome check
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] != s[j] or not is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = False
        
        ret = list()  # Store all partition results
        ans = list() # Current partition path

        def backtrack(start):
            if start == n:  # Partition complete
                ret.append(ans[:])  # Add current partition result
                return
            
            for end in range(start, n):
                if is_palindrome[start][end]:  # If s[start:end+1] is a palindrome
                    ans.append(s[start:end + 1])
                    backtrack(end + 1)  # Recursively process next partition point
                    ans.pop()
                # If not, skip directly
        
        backtrack(0)
        return ret

# Time complexity O(n * 2^n): n is string partition length, there are 2^(n-1) possible partitions
# Space complexity O(n^2): size of is_palindrome array
# Space complexity of backtracking O(n): store current partition path



# Backtracking + Memoization Search
# Checking palindrome can also use memoization search
class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = list()  # Store all partition results
        ans = list()  # Current partition path
        
        @cache
        def isPalindrome(i: int, j: int) -> bool:
            if i >= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        def backtrack(start: int):
            if start == n:
                res.append(ans[:])  # Add current partition result
                return
            
            for end in range(start, n):
                if isPalindrome(start, end) == 1:
                    ans.append(s[start:end + 1])
                    backtrack(end + 1)  # Recursively process next partition point
                    ans.pop()
                # If not, skip directly
        
        backtrack(0)
        return res