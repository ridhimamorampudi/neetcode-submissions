class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        mmap = defaultdict(list)
        queue = deque()
        count = 0

        for u,v in prerequisites:
            indegree[u] += 1
            if v in mmap[u]:
                return False
            mmap[v].append(u)
            count+= 1
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
            
        while queue:
            print(queue)
            curr = queue.popleft()
            for neigh in mmap[curr]:
                queue.append(neigh)
                indegree[neigh] -= 1
                count -= 1
        
        
        print(indegree)
        
        if queue or count != 0: return False
        return True
