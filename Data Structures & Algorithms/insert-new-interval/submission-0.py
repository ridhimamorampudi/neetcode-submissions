import bisect
class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for start,end in intervals:
            res.append(start)
        index = bisect.bisect_left(res,newInterval[0])
        
        intervals.insert(index,newInterval)
        res = [intervals[0]]
        for start,end in (intervals)[1:]:
            print(start)
            print()
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1],end)
            else:
                res.append([start,end])
        return res
