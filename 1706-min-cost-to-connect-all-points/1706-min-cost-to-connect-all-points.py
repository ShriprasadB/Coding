class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = [i for i in range(n)]
        all_edges = []
        cost = 0

        for i in range(n):
            for j in range(i+1, n):
                distance = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                all_edges.append([i, j, distance])
        
        all_edges.sort(key = lambda x: x[2])

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(n1, n2):
            nonlocal n
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return

            parent[p2] = p1
            n -= 1
            
        for x, y, w in all_edges:
            if find(x) != find(y):
                union(x, y)
                cost += w

        return cost if n == 1 else -1



'''
        n = len(points)
        adj = {}
        minheap = [[0, 0]]
        visited = set()
        res = 0
        
        for i in range(n):
            adj[i] = []
        
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([distance, j])
                adj[j].append([distance, i])
                
        
        while len(visited) < n:
            
            cost, i = heapq.heappop(minheap)
            
            if i in visited:
                continue
            
            visited.add(i)
            res += cost
            
            for nei_cost, nei in adj[i]:
                if nei not in visited:
                    heapq.heappush(minheap, [nei_cost, nei])
                
        return res

'''