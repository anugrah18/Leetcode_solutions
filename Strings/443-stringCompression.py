class Solution:
    #approach 1
    def compress_1(self, chars):
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

    # approach 2
    def compress_2(self, chars):
        readIndex = writeIndex = 0

        while readIndex < len(chars):
            count = 0
            letter = chars[readIndex]
            while readIndex < len(chars) and chars[readIndex] == letter:
                readIndex += 1
                count += 1

            chars[writeIndex] = letter
            writeIndex += 1
            if count > 1:
                for s in str(count):
                    chars[writeIndex] = s
                    writeIndex += 1

        return writeIndex




X = Solution()
print(X.compress_1(["a","a","b","b","c","c","c"]))
print(X.compress_2(["a","a","b","b","c","c","c"]))






