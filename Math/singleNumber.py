class Solution(object):
    def singleNumber(self, nums):
        return 2 * sum(set(nums)) - sum(nums)


X= Solution()
series = [1,2,1,2,4,3,3]
print(X.singleNumber(series))