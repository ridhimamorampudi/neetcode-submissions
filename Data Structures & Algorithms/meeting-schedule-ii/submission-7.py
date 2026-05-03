"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda i:i.start)
        #only keeps track of end times
        heap = []

        for interval in intervals:
            #if no overlap reuse that room
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            #push new interval
            heapq.heappush(heap,interval.end)
        
        return len(heap)
            


        