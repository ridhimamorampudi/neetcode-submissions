class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        topo = []
        q = deque([i for i in range(len(indegree)) if indegree[i] == 0 ])
        print(q)
        while q:
            node = q.popleft()
            topo.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return len(topo) == numCourses