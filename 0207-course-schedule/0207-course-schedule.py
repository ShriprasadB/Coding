class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegree = [0]*numCourses
        adj = collections.defaultdict(list)
        
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        
        q = []
        visited = set()

        for i in range(numCourses):
            if not indegree[i]:
                q.append(i)        

        while q:
            node = q.pop(0)
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        q.append(nei)
            
        return len(visited) == numCourses