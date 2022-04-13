class Solution:
    def combinationSum(self, candidates, target):

        result = []

        def backtrack(remain, comb, start):
            if remain == 0:
                result.append(list(comb))
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, i)

                comb.pop()

        backtrack(target, [], 0)
        return result

X = Solution()
print(X.combinationSum([2,3,6,7],7))