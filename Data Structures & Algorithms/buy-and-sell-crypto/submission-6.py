class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0 index means the initial day 
        # you only sell if you make a profit , if not 0 
        # you want to buy at the lowest rate and sell in the highest
        lowest=prices[0]
        profit =0

        for i in range(1, len(prices)):
            profit=max(prices[i]-lowest, profit)
            lowest=min(lowest, prices[i])
        return profit
