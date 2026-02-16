# Non-duplicate array, select elements to satisfy condition, check if it's a feasible solution

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(start=0, path=[], total=0):
            # If selected current node and get a feasible solution
            if total == target:
                res.append(path[:])
                print(res)
                return
            
            # Not a feasible solution, skip
            if total > target:
                return
            
            # Iterate to last number, recursion ends
            for i in range(start, len(candidates)):
                # Make choice, pick candidates[i]
                path.append(candidates[i])
                total += candidates[i]

                # Recursion, process next number
                backtrack(i, path, total)

                # Undo choice, don't pick candidates[i]
                path.pop()
                total -= candidates[i]

        res = []
        backtrack()
        return res