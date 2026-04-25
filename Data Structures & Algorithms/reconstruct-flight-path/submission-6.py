class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)

        #way #2: build it in reverse

 
        #build adjacency list
        for src,dst in tickets:
            adj_list[src].append(dst)
            adj_list[src].sort(reverse= True)
        #smallest vals at the back

        res = []

        def dfs(src):
            #go through starting vals at JFK
            while adj_list[src]:
                #first smallest dst
                dst = adj_list[src].pop()
                dfs(dst)
            #if it cannot work append it to the end 
            res.append(src)
        
        dfs("JFK")
        return res[::-1]



        
        


        



        


        