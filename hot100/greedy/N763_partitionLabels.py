# Same letter appears in at most one fragment
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Analyze time complexity, at least one traversal needed O(N)

        # First traversal, find the last appearance index of each letter
        last = [0] * 26
        for i, ch in enumerate(s):
            last[ord(ch) - ord("a")] = i
        
        partition = list()
        # Maintain current valid substring
        start = end = 0
        for i, ch in enumerate(s):
            # Current letter joins
            end = max(end, last[ord(ch) - ord("a")])
            if i == end: # Does not break current sequence validity
                partition.append(end - start + 1)
                # Next subsequence
                start = end + 1
        
        return partition
