"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap =[]
        intervals.sort(key=lambda i: i.start)

        for interval in intervals:
            print(interval.start)
            
            if not heap or interval.start < heap[0][0]:
                print("here")
                
                heapq.heappush(heap,(interval.end,interval.start))
            else:
                heapq.heappushpop(heap,(interval.end,interval.start))
        
        return len(heap)

