class Solution(object):
    def strStr(self, haystack, needle):
        if (needle == ""):
            return 0
        m = len(haystack)
        n = len(needle)

        if (m < n):
            return -1

        for i in range(0, m - n + 1):
            for j in range(0, n):
                if (haystack[i + j] != needle[j]):
                    break
                if (j == n - 1):
                    return i

        return -1

X = Solution()
print(X.strStr("liver","ve"))