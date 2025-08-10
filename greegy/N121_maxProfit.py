class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        # 我们用一个变量记录截止目前为止的历史低点
        # 遍历数组，记录当天卖出能赚多少钱

        # 贪心：我们总是在过往的最低点买入
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                 min_price = price
            else:
                res = max(res, price - min_price)
        
        return res