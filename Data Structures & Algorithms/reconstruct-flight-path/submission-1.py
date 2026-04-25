class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        #lexigraphically small
        for t in sorted(tickets)[::-1]:
            adj_list[t[0]].append(t[1])
            adj_list[t[0]][::-1]

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
        



        


        