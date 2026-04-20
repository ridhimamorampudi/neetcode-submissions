class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #adjacency matrix
        graph = defaultdict(list)
        #indegree
        indegree = [0]*numCourses

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1

        q = deque([i for i in range(len(indegree)) if indegree[i] == 0])
        topo = []

        while q:
            node = q.pop()
            topo.append(node)
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(topo) == numCourses:
            return topo
        return []