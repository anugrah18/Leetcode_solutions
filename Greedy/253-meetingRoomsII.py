class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if not intervals:
            return 0

        res, rooms = 0, 0
        startTimings = [0] * len(intervals)
        endTimings = [0] * len(intervals)

        e = 0
        s = 0

        for i in range(len(intervals)):
            startTimings[i] = intervals[i][0]

        for i in range(len(intervals)):
            endTimings[i] = intervals[i][1]

        startTimings.sort()
        endTimings.sort()

        while s < len(intervals):
            if startTimings[s] < endTimings[e]:
                s += 1
                rooms += 1
            else:
                e += 1
                rooms -= 1
            res = max(rooms, res)

        return res


X = Solution()
print(X.minMeetingRooms([[0,30],[5,10],[15,20]]))
