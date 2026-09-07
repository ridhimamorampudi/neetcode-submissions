class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for i in range(n+1)]
        shortest = [float('inf')]*(n+1)

        for src,dst,time in times:
            adj[src].append([dst,time])
        
        heap = []
        shortest[k] = 0
        heapq.heappush(heap,(0,k))

        while heap:
            currTime,curr = heapq.heappop(heap)

            if currTime > shortest[curr]:
                continue
            for nei,time in adj[curr]:
                newTime = currTime + time
                if newTime < shortest[nei]:
                    shortest[nei] = newTime
                    heapq.heappush(heap,(newTime,nei))
        
        ans = max(shortest[1:])
        if ans == float('inf'):
            return -1
        return ans