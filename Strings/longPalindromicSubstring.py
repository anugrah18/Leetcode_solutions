class Solution:
    _resStart = 0
    _resLength = 0

    def longestPalindrome(self,s):
        for i in range(0,len(s)):
            self._expandFromMiddle(s,i,i)
            self._expandFromMiddle(s,i,i+1)

        return s[self._resStart:self._resStart+self._resLength]

    def _expandFromMiddle(self,s,left,right):

        while(left>=0 and right<len(s) and s[left]==s[right]):
            left = left-1
            right = right+1

        if(self._resLength<right-left-1):
            self._resStart = left + 1
            self._resLength = right-left-1

X = Solution()
print(X.longestPalindrome("bhdbabbajnfjnfg"))