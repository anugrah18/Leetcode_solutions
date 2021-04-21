class Solution:
    def numPairsDivisibleBy60(self,time):
        dict = {}
        res = 0

        for t in time:
            if ((60-t)%60) not in dict:
                dict[(60-t)%60]=0
            if t%60 not in dict:
                dict[t%60] = 0

            res += dict[(60-t)%60]
            dict[t%60]+=1

        return res

X = Solution()
print(X.numPairsDivisibleBy60([30,20,150,100,40]))
