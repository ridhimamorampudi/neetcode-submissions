class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)
        res = []
        res.append(intervals[0])
        for i in range(1,n):
            # merged
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
        
        return res



        #start of second interval < end of first interval
        #1  2 3 4 5 6 7