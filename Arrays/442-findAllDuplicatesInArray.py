class Solution:
    def findDuplicates(self, nums):

        ans = []

        for num in nums:
            nums[abs(num) - 1] *= -1

        for num in nums:
            if (nums[abs(num) - 1] > 0):
                ans.append(abs(num))
                nums[abs(num) - 1] *= -1

        return ans


X = Solution()
print(X.findDuplicates([4,3,2,7,8,2,3,1]))