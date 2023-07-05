class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj = {}
        pq = [(0, k)]
        visited = set()
        time = 0
        adj = collections.defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))
            
        while pq:
            weight, node = heapq.heappop(pq)
            if node in visited:
                continue
            
            visited.add(node)
            time = max(time, weight)
            
            for nei, w2 in adj[node]:
                if nei not in visited:
                    heapq.heappush(pq, (weight + w2, nei))
            
        return time if len(visited) == n else -1
            
        