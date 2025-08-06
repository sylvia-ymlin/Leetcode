# it requires as to find the 异位词 of s in p
# the 异位词 is a permutation of the string, they have the same characters
# so we keep a sliding window of length len(p)
# we use a dictionary to count the characters in p
# we need to return the starting indices of the substrings in s

from typing import List
from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []

        if len(p) > len(s):
            return res
        
        n = len(p)

        charCount = [0] * 26

        for char in p:
            charCount[ord(char) - ord('a')] += 1

        curCharCount = [0] * 26

        for i in range(n):
            curCharCount[ord(s[i]) - ord('a')] += 1
        
        if curCharCount == charCount:
            res.append(0)

        l, r = 1, n
        while r < len(s):
            curCharCount[ord(s[l - 1]) - ord('a')] -= 1
            curCharCount[ord(s[r]) - ord('a')] += 1

            if curCharCount == charCount:
                res.append(l)
            
            l += 1
            r += 1

        
        return res

# test
s = "cbaebabacd"
p = "abc"

sol = Solution()
result = sol.findAnagrams(s, p)
print(result)  # Output: [0, 6], because "cba" and "bac" are the anagrams of "abc"