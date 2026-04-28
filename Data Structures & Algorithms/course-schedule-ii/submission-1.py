class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        mmap = defaultdict(list)
        q = deque()
        count = 0
        res = []

        for course,prereq in prerequisites:
            indegree[course] += 1
            mmap[prereq].append(course)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            curr = q.popleft()
            res.append(curr)
            count += 1
            for n in mmap[curr]:
                indegree[n]-=1
                if indegree[n] == 0:
                    q.append(n)
        
        if count != numCourses:
            return []
        else:
            return res
            