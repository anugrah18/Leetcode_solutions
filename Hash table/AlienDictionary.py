class Solution:
    def isAlienSorted(self,words,order):
        ht = {}

        for i in range(0,len(order)):
            ht[order[i]]=i

        for i in range(1,len(words)):
            if(self._comparer(words[i-1],words[i],ht) >0):
                return False

        return True


    def _comparer(self,word1,word2,ht):
        i = 0
        j = 0
        char_compare = 0

        while(i<len(word1) and j<len(word2) and char_compare==0):
            char_compare = ht[word1[i]]-ht[word2[j]]

        if(char_compare == 0):
            return len(word1)-len(word2)
        else:
            return char_compare

X = Solution()
print(X.isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz"))