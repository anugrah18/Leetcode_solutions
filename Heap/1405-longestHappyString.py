import heapq
class Solution:
    def longestDiverseString(self, a, b, c) -> str:
        res, maxHeap = "", []
        dict = {}
        dict["a"] = -a
        dict["b"] = -b
        dict["c"] = -c

        for k in dict:
            if dict[k] != 0:
                heapq.heappush(maxHeap, (dict[k], k))

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                res += char
                count += 1
            if count:
                heapq.heappush(maxHeap, (count, char))

        return res

X = Solution()
print(X.longestDiverseString(1,1,7))