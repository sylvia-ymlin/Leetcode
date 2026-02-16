from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] indicates whether s[0:i] can be segmented by wordDict
        # State transition equation
        # dp[i] = dp[j] and s[j:i] in wordDict for each j < i

        # set() quickly check if it is a valid word
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            # Enumerate all possible j, must enumerate by existing word lengths
            for word in wordSet:
                word_len = len(word)
                if i >= word_len and s[i - word_len:i] == word and dp[i - word_len]:
                    dp[i] = True
                    break

        return dp[n]
