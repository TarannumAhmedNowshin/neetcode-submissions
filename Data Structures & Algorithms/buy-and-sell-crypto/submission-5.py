class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0 index means the initial day 
        # you only sell if you make a profit , if not 0 
        # you want to buy at the lowest rate and sell in the highest
        maxx=0
        profit=0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
            
                profit=prices[j]-prices[i]

                
                maxx=max(profit,maxx)
        return maxx

