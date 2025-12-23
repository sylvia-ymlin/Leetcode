# 将一个子串分割为回文字符串
from linecache import cache
from typing import List

# 回溯 + 动态规划
# 回溯用于生成所有可能的分割方式
# 动态规划用于判断子串是否为回文

# 需要找到分割方式
# start：当前分割起点
# [0, start) 之前的子串已经是回文, 寻找 [start, end] 的分割
# 如果 搜索到 end == len(s)，说明已经分割完毕，将当前分割结果添加到结果集中
# 回溯，删除 当前分割点，继续搜索

# 判断子串是否为回文
# 动态规划数组 is_palindrome[i][j] 表示 s[i:j] 是否为回文


class Solution1:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        is_palindrome = [[True] * n for _ in range(n)]

        # 初始化回文判断
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] != s[j] or not is_palindrome[i + 1][j - 1]:
                    is_palindrome[i][j] = False
        
        ret = list()  # 存储所有分割结果
        ans = list() # 当前分割路径

        def backtrack(start):
            if start == n:  # 分割完毕
                ret.append(ans[:])  # 添加当前分割结果
                return
            
            for end in range(start, n):
                if is_palindrome[start][end]:  # 如果 s[start:end+1] 是回文
                    ans.append(s[start:end + 1])
                    backtrack(end + 1)  # 递归处理下一个分割点
                    ans.pop()
                # 不是，直接跳过
        
        backtrack(0)
        return ret

# 时间复杂度 O(n * 2^n): n 是字符串分割长度，字符串分割方式有 2^(n-1) 种可能
# 空间复杂度 O(n^2): is_palindrome 数组的大小
# 回溯的空间复杂度 O(n): 存储当前分割路径



# 回溯 + 记忆化搜索
# 判断是否是回文串也可以用记忆搜索
class Solution2:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = list()  # 存储所有分割结果
        ans = list()  # 当前分割路径
        
        @cache
        def isPalindrome(i: int, j: int) -> bool:
            if i >= j:
                return 1
            return isPalindrome(i + 1, j - 1) if s[i] == s[j] else -1

        def backtrack(start: int):
            if start == n:
                res.append(ans[:])  # 添加当前分割结果
                return
            
            for end in range(start, n):
                if isPalindrome(start, end) == 1:
                    ans.append(s[start:end + 1])
                    backtrack(end + 1)  # 递归处理下一个分割点
                    ans.pop()
                # 不是，直接跳过
        
        backtrack(0)
        return res