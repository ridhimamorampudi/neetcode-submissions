class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        t = 0  
        
        for src,tar,ti in times:
            adj[src].append([tar,ti])
        
        shortest = {}

        heap = []
        heapq.heappush(heap,[0,k])

        while heap:
            totalTime, node = heapq.heappop(heap)
            if node in shortest:
                continue
            shortest[node]=totalTime
            t = totalTime

            for nei,nWeight in adj[node]:
                if nei not in shortest:
                    heapq.heappush(heap,[nWeight+totalTime,nei])
        
        return t if len(shortest) == n else -1
