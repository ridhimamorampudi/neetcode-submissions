class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for point in points:
            val = math.pow((math.pow(point[0],2) + math.pow(point[1],2)),1/2)
            heapq.heappush(h,(-val,point))
            if len(h) > k:
                heapq.heappop(h)

        return [point[1] for point in h]

