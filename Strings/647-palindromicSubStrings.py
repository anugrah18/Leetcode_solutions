class Solution:
    count = 0

    def countSubstrings(self, s):
        for i in range(len(s)):
            self.expandFromMiddle(s, i, i)
            self.expandFromMiddle(s, i, i + 1)
        return self.count

    def expandFromMiddle(self, s, i, j):
        while (i >= 0 and j < len(s) and s[i] == s[j]):
            self.count += 1
            i -= 1
            j += 1

X =Solution()
print(X.countSubstrings("abc"))