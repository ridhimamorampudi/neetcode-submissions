class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 1 2 3 4 5 6 7

        # [[1,2][1,4][1,5][2,4]]
        # [1,5]
        # [6,7]

        #greedily pick the smaller end time if there is overlap

        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start,end in intervals[1:]:
            #no overlap
            if prevEnd <= start:
                prevEnd = end
            #yes overlap
            else:
                res += 1
                prevEnd = min(end,prevEnd)
        return res

