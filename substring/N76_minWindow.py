# find the smallest substring in s that contains all characters in t

# using sliding window, and traverse the string s once

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1


        have, need = 0, len(countT)
        res = [-1, -1]  # start, end, we need to return the substring
        resLen = float("inf") # the minimum length of the substring found

        l = 0
        for r in range(len(s)): # always move the right pointer
            # check
            # current character
            char = s[r]
            # current window count
            window[char] = window.get(char, 0) + 1

            if char in countT and window[char] == countT[char]: # we have enough number of this character in current window, and only count once
                have += 1
            
            # when we find a valid substring
            while have == need: # we have all characters with enough frequency
                # check whether the window is smaller than the previous one
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # move the window to the right
                window[s[l]] -= 1
                # if the moving out character is what we need
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                # move the left, check for the nextwindow
                l += 1
        
        # we need to return the substring
        l, r = res

        return s[l:r + 1] if resLen != float("inf") else ""
 # so the key idea is, we need the current window have enough characters we need, we only care about the characters in t