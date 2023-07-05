class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = collections.defaultdict(list)

        for i, (x, y) in enumerate(edges):
            adj[x].append([succProb[i],y])
            adj[y].append([succProb[i],x])

        pq = [(-1, start)]
        visit = set()

        while pq:
            prob, node = heapq.heappop(pq)
            visit.add(node)

            if node == end:
                return prob*-1

            for p, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(pq, (prob*p, nei))
        
        return 0