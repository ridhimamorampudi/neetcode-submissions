class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)

        #sorted sorts nested lists by first sortng within the list
        #then sorts all of them

        #lexigraphically small
        #sorted first sorts the

        #want to sort by second value of nested list (dest) 
        
        for t in tickets:
            adj_list[t[0]].append(t[1])
            adj_list[t[0]].sort(reverse=True)

        res = []
        
        #do dfs to find a valid path
        #do bfs to find smallest path

        def dfs(src):
            while adj_list[src]:
                dst = adj_list[src].pop()
                dfs(dst)
            res.append(src)

        dfs("JFK")
        return res[::-1]
        



        


        