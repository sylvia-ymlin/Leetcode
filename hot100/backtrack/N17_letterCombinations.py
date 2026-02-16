class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Also a permutation problem
        # 2 - 9
        # 2: "abc"
        # 3: "def"
        # 4: "ghi"
        # 5: "jkl"
        # 6: "mno"
        # 7: "pqrs"
        # 8: "tuv"
        # 9: "wxyz"

        # Each key has three (or 9 corresponds to four) choices

        # Array length may be 0
        if len(digits) == 0:
            return []
        
        phone_map = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def backtrack(index=0, path=""):
            # If current path length equals digits length, a feasible solution is found
            if len(path) == len(digits):
                res.append(path)
                return
            
            # Get letters corresponding to current digit
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                # Make choices
                path += letter

                # Recursively process next digit
                backtrack(index + 1, path)
                
                # Undo choice
                path = path[:-1]
        
        res = []
        backtrack()
        return res