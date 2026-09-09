class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[1])
        count = 0
        res = []

        print(intervals)

        for interval in intervals:
            if not res or interval[0] >= res[-1][1]:
                res.append(interval)
            else:
                count += 1

        return count


