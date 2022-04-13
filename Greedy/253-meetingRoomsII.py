class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        rooms = 0
        startTimings = [0] * len(intervals)
        endTimings = [0] * len(intervals)
        L = len(intervals)
        end_pointer = 0
        start_pointer = 0

        for i in range(len(intervals)):
            startTimings[i] = intervals[i][0]

        for i in range(len(intervals)):
            endTimings[i] = intervals[i][1]

        startTimings.sort()
        endTimings.sort()

        while start_pointer < L:
            if startTimings[start_pointer] >= endTimings[end_pointer]:
                rooms -= 1
                end_pointer += 1

            rooms += 1
            start_pointer += 1

        return rooms


X = Solution()
print(X.minMeetingRooms([[0,30],[5,10],[15,20]]))
