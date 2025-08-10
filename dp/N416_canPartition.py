class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 从数组中选出一些数字，使得这些数字的和等于整个数组的元素和的一半
        # 0-1 背包问题，是否选择当前元素
        # dp[i][j]: 表示从数组 [0, i] 是否存在和为 j 的序列

        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        # dp[0] = True 和为 0 的子集一定存在 （空集）
        dp = [True] + [False] * target
        for num in nums:
            # dp[j] 以 i 结尾，是否存在 和 为 target 的子集
            for j in range(target, num - 1, -1):
                # 已经得到 dp[j] == True，直接返回
                # dp[j] 还不是 true, 但是知道 dp[j-num] true
                # 那么加上当前的 num，刚好是 j，可以 return true
                dp[j] |= dp[j - num]
        
        return dp[target]
