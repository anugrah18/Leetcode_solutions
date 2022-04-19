class Solution(object):
    # Approach 1 : using set.
    def lengthOfLongestSubstring_I(self, s: str) -> int:
        cSet = set()
        ans = 0
        l = 0
        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1

            cSet.add(s[r])
            ans = max(ans, r - l + 1)

        return ans

    # Approach 2 : using hash.
    def lengthOfLongestSubstring_II(self, s):
        dict = {}
        ans = 0
        i = 0
        j = 0

        while (i < len(s) and j < len(s)):
            if (s[j] not in dict):
                dict[s[j]] = s[j]
                j = j + 1
                ans = max(ans, j - i)
            else:
                dict.pop(s[i])
                i = i + 1
        return ans


X = Solution()
print(X.lengthOfLongestSubstring_I("xcwxcabcxc"))
print(X.lengthOfLongestSubstring_II("xcwxcabcxc"))