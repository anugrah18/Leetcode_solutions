class Solution:
    def compress(self, chars):
        stack = []
        count = 1
        ans = ""

        for c in chars:
            if len(stack) == 0:
                stack.append(c)
            elif c in stack[-1]:
                count += 1
            else:
                ans = ans + stack.pop()
                if (count > 1):
                    ans = ans + str(count)
                count = 1
                stack.append(c)

        if (len(stack) != 0):
            ans = ans + stack.pop()
            if (count > 1):
                ans = ans + str(count)

        N = min(len(ans), len(chars))

        if (N == len(ans)):
            for i in range(0, N):
                chars[i] = ans[i]

        return N

X = Solution()
print(X.compress(["a","a","b","b","c","c","c"]))







