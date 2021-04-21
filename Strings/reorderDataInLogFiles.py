class Solution:
    def reorderLogFiles(self,logs):
        return sorted(logs,key=self.get_key)

    def get_key(self,log):
        _id,rest = self.splitLogs(log)
        if(rest[0].isalpha()):
            return(0,rest,_id)
        else:
            return(1,)


    def splitLogs(self,log):
        for i,c in enumerate(log):
            if(i==""):
                break
            return (log[:i],log[i+1:])

X = Solution()
print(X.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))