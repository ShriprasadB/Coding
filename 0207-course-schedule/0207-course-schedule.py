class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegree = [0]*numCourses
        adj = collections.defaultdict(list)

        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        
        q = []
        visited = 0

        for i in range(numCourses):
            if not indegree[i]:
                q.append(i)        

        while q:
            node = q.pop(0)
            visited += 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
            
        return visited == numCourses