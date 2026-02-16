class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        # We use a variable to record the historical low point up to now
        # Iterate through the array, record how much profit can be made if sold today

        # Greedy: we always buy at the past lowest point
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                 min_price = price
            else:
                res = max(res, price - min_price)
        
        return res