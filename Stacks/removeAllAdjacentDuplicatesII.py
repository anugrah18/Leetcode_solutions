class Solution:
    def RemoveDuplicate(self,s,k):
        stack = []
        i = 0

        while(i<len(s)):
            if(i==0 or s[i]!=s[i-1]):
                stack.append(1)
            if(stack[-1]==k):
                stack.pop()
                s = s[0:i-k+1]+s[i+1:]
                i = i-k
            else:
                stack[-1]+=1
            i+=1
        return s

X = Solution()
print(X.RemoveDuplicate("deeedbbcccbdaa",3))