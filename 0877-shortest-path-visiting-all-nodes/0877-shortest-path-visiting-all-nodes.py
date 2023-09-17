class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:        
        n = len(graph)
        q = deque([(node, 1 << node) for node in range(n)]) # (node, visit_status)
        visit = set(q) # (node, visit_status)
        ending_mask = (1 << n) - 1
        step = 0

        while q:
            for _ in range(len(q)):
                node, mask = q.popleft()

                if mask == ending_mask:
                    return step

                for nxt in graph[node]:
                    nxt_mask = mask | (1<<nxt)
                    
                    if (nxt, nxt_mask) not in visit:
                        q.append((nxt, nxt_mask))
                        visit.add((nxt, nxt_mask))
            step += 1