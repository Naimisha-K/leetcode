class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=prices[0]
        profit=0
        for i in prices:
            m=min(m,i)
            p=i-m
            profit=max(profit,p)
        return profit