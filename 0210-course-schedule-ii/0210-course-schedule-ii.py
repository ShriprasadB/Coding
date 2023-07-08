class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[] for i in range(numCourses)]
        indeg=[0]*numCourses
        for u, v in prerequisites:
            adj[v].append(u)
            indeg[u] += 1
        
        res = []
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        while q:
            u = q.popleft()
            res.append(u)
            for i in adj[u]:
                if indeg[i] != 0:
                    indeg[i] -= 1
                if indeg[i] == 0:
                    q.append(i)
                    
        return [] if len(res) != numCourses else res