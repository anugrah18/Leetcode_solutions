class Solution(object):
    def leastInterval(self, tasks, n):

        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord('A')] += 1

        freq.sort()

        # max_frequency
        f_max = freq.pop()
        idle_time = (f_max - 1) * n

        while freq:
            idle_time -= min(f_max - 1, freq.pop())

        idle_time = max(0, idle_time)

        return idle_time + len(tasks)

X =Solution()
print(X.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2))