class Solution:
    def letterCombo(self,digits):

        if(digits == ""):
            return []

        dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        output = []
        output.append("")

        for i in range(len(digits)):
            curr = digits[i]
            while(len(output[0])==i):
                perm = output.pop(0)
                for c in dict[curr]:
                    output.append(perm+c)

        return output

X = Solution()
print(X.letterCombo("23"))