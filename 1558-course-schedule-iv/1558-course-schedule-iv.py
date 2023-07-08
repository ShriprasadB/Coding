class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        indegree = [0]*numCourses 
        for u, v in prerequisites : 
            adj[u].add(v)
            indegree[v] += 1 
        
        q = []
        req = defaultdict(set)
        
        for i in range(numCourses):
            if indegree[i] == 0 : 
                q.append(i)
        
        while q: 
            node = q.pop(0)
            for nei in adj[node]:
                indegree[nei] -= 1 
                if indegree[nei] == 0 : 
                    q.append(nei)
        
                req[nei].add(node)
                for el in req[node]:
                    req[nei].add(el)
                
        ans = []
        for u , v in queries: 
            if u in req[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans 