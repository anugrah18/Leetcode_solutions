class Solution(object):
    def partitionLabels(self, S):

        if (len(S) == 0):
            return None

        ans = []
        ch = [0] * 26

        # Get last index of that character in String
        for i in range(len(S)):
            ch[ord(S[i]) - ord('a')] = i

        start = 0
        end = 0

        for i in range(len(S)):
            end = max(end, ch[ord(S[i]) - ord('a')])

            if (i == end):
                ans.append(end - start + 1)
                start = end + 1

        return ans

X =Solution()
print(X.partitionLabels("ababcbacadefegdehijhklij"))