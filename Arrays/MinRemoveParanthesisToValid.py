class Solution:
    def minRemoveToMakeValid(self,s):
        index_to_remove = set()
        stack = []

        for i,c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif len(stack)==0:
                index_to_remove.add(i)
            else:
                stack.pop()

        index_to_remove  = index_to_remove.union(set(stack))
        ans = []
        for i,c in enumerate(s):
            if i not in index_to_remove:
                ans.append(c)

        return "".join(ans)

X = Solution()
print(X.minRemoveToMakeValid("(a(b(c)d)"))
