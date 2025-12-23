# no repeated, so we need to choose a data structure that allows us to store no repeated elements, that is, a set

from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        # sliding window
        l , r = 0, 0
        # record the longest length
        res = 0
        while r < len(s):
            if s[r] not in charSet: # add to the set
                charSet.add(s[r])
                r += 1 # move the right pointer
                res = max(res, r - l) # update the longest length
            else:
                charSet.remove(s[l]) # remove
                l += 1              # until we remove the repeated character

        return res