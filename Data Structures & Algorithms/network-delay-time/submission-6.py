class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

       
        #list of src -> target
        graph = defaultdict(list)

        #keeps track of min times
        shortest = [float('inf')]*(n+1)

        #collect all values of nodes
        for src,tar,ti in times:
            graph[src].append((tar,ti))
        
        
        shortest[k] = 0
        heap = []
        heapq.heappush(heap,(0,k))
        
        while heap:
            currTime,curr = heapq.heappop(heap)
            
            if currTime > shortest[curr]:
                continue
            
            for neigh,time in graph[curr]:
                newTime = currTime+time
                if newTime < shortest[neigh]:
                    shortest[neigh] = newTime
                    heapq.heappush(heap,(newTime,neigh))
        
        ans = max(shortest[1:])
        if ans == float('inf'):
            return -1
        
        return ans

        
            