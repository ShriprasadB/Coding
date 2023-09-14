class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        tickets.sort()
        res = ["JFK"]
        
        for s, d in tickets:    
            if s not in adj:
                adj[s] = [d]
            else:
                adj[s].append(d)
       
            
        def dfs(source):
            
            if len(res) == len(tickets) + 1:
                return True
            
            if source not in adj:
                return False
            
            temp = adj[source]
            for i, dst in enumerate(temp):
                
                adj[source].pop(i)
                res.append(dst)
                
                if dfs(dst):
                    return True
                
                adj[source].insert(i, dst)
                res.pop()
            
            return False
            
        dfs("JFK")
        
        return res
        