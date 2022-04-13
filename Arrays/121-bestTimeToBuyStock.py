class Solution(object):
    def maxProfit(self, prices):
        if(len(prices)==0):
            return 0
        minStock = prices[0]
        i = 1
        maxProfit = 0

        while(i<len(prices)):
            if(prices[i]<minStock):
                minStock = prices[i]
            else:
                profit = prices[i]-minStock
                if profit > maxProfit:
                    maxProfit = profit
            i = i+1
        return maxProfit


X = Solution()
print(X.maxProfit([7,1,5,3,6,4]))


