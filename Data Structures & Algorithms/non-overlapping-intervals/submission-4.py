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
        ans = []
        ans.append(intervals[0])

        for start,end in intervals[1:]:
            #no overlap
            if ans[-1][1] <= start:
                prevEnd = end
                ans.append([start,end])
            #yes overlap
            else:
                res += 1
                if ans[-1][1] > end:
                    ans[-1][1] = end
        
        return len(intervals)-len(ans)

