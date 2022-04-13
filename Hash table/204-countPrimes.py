class Solution(object):
    def countPrimes(self, n):
        if (n < 3):
            return 0
        dict = {}
        count = 0

        for i in range(2, n):
            dict[i] = True

        dict[n] = False

        for i in range(2, n + 1):
            if (dict[i] == True):
                for j in range(2, int(n / i) + 1):
                    dict[i * j] = False;

        for i in dict:
            if (dict[i] == True):
                count = count + 1

        return count

X =Solution()
print(X.countPrimes(10))





