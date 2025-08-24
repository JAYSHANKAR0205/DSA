class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minm=prices[0]
        profit=0
        for i in range(1,len(prices)):
            cost=prices[i]-minm
            minm=min(prices[i],minm)
            profit=max(cost,profit)
        return profit


        