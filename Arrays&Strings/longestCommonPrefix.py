class Solution(object):
    def longestCommonPrefix(self,strs):
        if(len(strs)==""):
            return ""

        prefix = strs[0]

        for i in range(0,len(strs)):
            while(strs[i].find(prefix)!=0):
                prefix = prefix[:-1]

        return prefix


X = Solution()
print(X.longestCommonPrefix(["flower","flow","flight"]))