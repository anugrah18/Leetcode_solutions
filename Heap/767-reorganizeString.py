import heapq

class Solution:
    def reorganizeString(self,S):

        dict = {}

        for c in S:
            if c not in dict:
                dict[c]=0
            dict[c]-=1

        heap = []
        for k in dict:
            heap.append((dict[k],k))

        heapq.heapify(heap)
        ans = []
        while(len(heap)>=2):
            ncount1,nch1 = heapq.heappop(heap)
            ncount2, nch2 = heapq.heappop(heap)

            ans.extend([nch1,nch2])

            if(ncount1 + 1 !=0):
                heapq.heappush(heap,(ncount1+1,nch1))
            if(ncount2 + 1 != 0):
                heapq.heappush(heap, (ncount2+1, nch2))

        ans = "".join(ans)

        if heap:
            ans = ans+heap[0][1]

        if len(ans) == len(S):
            return ans
        else:
            return ""

X = Solution()
print(X.reorganizeString('abba'))



