class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        ans = []
        ans.append(intervals[0])

        for start,end in intervals[1:]:

            if ans[-1][1] <= start:
                ans.append([start,end])

            else:
                ans[-1][1] = min(ans[-1][1],end)
        
        return len(intervals)-len(ans)

