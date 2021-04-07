class Solution:
    def removeDuplicates(self,S):
        stack = []

        for c in S:
            if(len(stack)==0):
                stack.append(c)
            elif c==stack[-1]:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)

X = Solution()
print(X.removeDuplicates("abbaca"))