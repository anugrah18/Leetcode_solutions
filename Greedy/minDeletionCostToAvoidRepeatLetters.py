class Solution:
    def minCost(self,s,cost):
        n = len(s)
        gsum = gmax = cost[0]
        ans = 0

        for i in range(1,n):
            if(s[i]!= s[i-1]):
                ans += gsum - gmax
                gsum = 0
                gmax = 0

            gsum += cost[i]
            gmax = max(gmax,cost[i])

        ans += gsum - gmax
        return ans
X= Solution()
print(X.minCost("abaac",[1,2,3,4,5]))