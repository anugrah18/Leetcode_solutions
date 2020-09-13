class Solution(object):
    def numDecodings(self, s):
        dp = [0] * (len(s) + 1)

        dp[0] = 1

        dp[1] = 1 if s[0] != "0" else 0

        for i in range(2, len(dp)):
            if (s[i - 1] != "0"):
                dp[i] = dp[i] + dp[i - 1]
            num = int(s[i - 2:i])
            if (num >= 10 and num <= 26):
                dp[i] = dp[i] + dp[i - 2]

        return dp[len(s)]

X = Solution()
print(X.numDecodings("125"))