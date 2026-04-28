class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        mmap = defaultdict(list)

        for src,dst in edges:
            mmap[src].append(dst)
            mmap[dst].append(src)
        
        visited = set()
        q = deque()
        q.append(0)
        visited.add(0)

        while q:
            curr = q.popleft()
            for ni in mmap[curr]:
                if ni not in visited:
                    visited.add(ni)
                    q.append(ni)

        return len(visited) == n


