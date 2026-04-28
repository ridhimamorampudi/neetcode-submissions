class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        mmap = defaultdict(list)
        queue = deque()
        count = 0

        for course,prereq in prerequisites:
            indegree[course] += 1
            mmap[prereq].append(course)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
            
        while queue:
            curr = queue.popleft()
            count += 1
            for neigh in mmap[curr]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)

        
        return count == numCourses
