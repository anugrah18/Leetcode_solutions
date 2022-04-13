class Solution:
    def reverseWords(self,s):
        s=s.split(" ")
        cleaned_s = []

        for c in s:
            if c!="":
                cleaned_s.append(c)

        cleaned_s = cleaned_s[::-1]

        return " ".join(cleaned_s)

X= Solution()
print(X.reverseWords("    Hello    World"))