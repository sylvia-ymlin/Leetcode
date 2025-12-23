from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] 表示 s[0:i] 是否可以被 wordDict 拆分
        # 状态转移方程
        # dp[i] = dp[j] and s[j:i] in wordDict for each j < i

        # set() 快速判断是否是合法单词
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            # 枚举所有可能的 j，一定是 按照 存在的单词长度来枚举
            for word in wordSet:
                word_len = len(word)
                if i >= word_len and s[i - word_len:i] == word and dp[i - word_len]:
                    dp[i] = True
                    break

        return dp[n]
