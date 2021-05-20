class Solution:
    def minDeletion(self,s):
        freq=[0]*26
        count=0

        for c in s:
            freq[ord(c)-ord('a')]+=1

        freq = sorted(freq,reverse=True)

        freq_limit = freq[0]-1

        for i in range(1,len(freq)):
            if freq[i]<=freq_limit:
                freq_limit = freq[i]-1
            else:
                count+= freq[i]-freq_limit
                freq_limit-=1

            freq_limit=max(freq_limit,0)

        return count

X = Solution()
print(X.minDeletion('aaabbbccc'))