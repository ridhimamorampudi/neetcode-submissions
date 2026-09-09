class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = []


        for interval in intervals:

            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                res[-1][0] = min(res[-1][0], interval[0])
                res[-1][1] = max(res[-1][1], interval[1])
                
        
        return res