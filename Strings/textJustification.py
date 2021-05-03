class Solution:
    def fullJustify(self, words, maxWidth):
        def leftJustify(words, diff, i, j):
            spacesOnRight = diff - (j - i - 1)
            result = words[i]
            for k in range(i + 1, j):
                result += " " + words[k]

            result += " " * spacesOnRight
            return result

        def middleJustify(words, diff, i, j):
            spaceNeeded = j - i - 1
            spaces = diff // spaceNeeded
            extraSpaces = diff % spaceNeeded

            result = words[i]
            for k in range(i + 1, j):
                spacesToApply = spaces + (1 if extraSpaces > 0 else 0)
                extraSpaces -= 1
                result += " " * spacesToApply + words[k]

            return result

        i = 0
        n = len(words)
        result = []
        while (i < n):
            j = i + 1
            lineLength = len(words[i])
            while (j < n and (lineLength + len(words[j]) + (j - i - 1) < maxWidth)):
                lineLength += len(words[j])
                j += 1

            diff = maxWidth - lineLength
            numberOfWords = j - i
            if (numberOfWords == 1 or j >= n):
                result.append(leftJustify(words, diff, i, j))
            else:
                result.append(middleJustify(words, diff, i, j))

            i = j

        return result


X = Solution()
print(X.fullJustify(["This", "is", "an", "example", "of", "text", "justification."],16))





