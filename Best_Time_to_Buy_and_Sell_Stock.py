class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #max=0
        i,j=0,0
        max_price=0
        while j<len(prices):
            if prices[j]>prices[i]:
                max_price=max(max_price, prices[j]-prices[i])
            else:
                i=j
            j+=1
        return max_price
       
        
