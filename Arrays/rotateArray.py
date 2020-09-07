class Solution(object):
    def rotate(self, nums, k):

        k = k% len(nums)
        nums[k:],nums[:k] = nums[:-k],nums[-k:]

        return nums

X =Solution()
print(X.rotate([1,2,3,4,5,6,7],4))