class Solution(object):
    def productExceptSelf(self, nums):
        L_To_R = [1] * len(nums)
        R_To_L = [1] * len(nums)
        answer = [0] * len(nums)

        for i in range(0, len(nums) - 1):
            L_To_R[i + 1] = nums[i] * L_To_R[i]

        for j in range(len(nums) - 1, 0, -1):
            R_To_L[j - 1] = nums[j] * R_To_L[j]

        for i in range(0, len(nums)):
            answer[i] = L_To_R[i] * R_To_L[i]

        return answer

X = Solution()
print(X.productExceptSelf([1,2,3,4,5]))