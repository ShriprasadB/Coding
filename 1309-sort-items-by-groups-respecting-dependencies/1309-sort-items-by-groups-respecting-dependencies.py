class Solution:
    def topsort(self, queue, out_edges, in_degree):
        ordering = []
        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                ordering.append(node)
                for nei in out_edges[node]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0:
                        queue.append(nei)
        return ordering

    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        heads = [n + 2*i for i in range(m)]
        tails = [n + (2*i) + 1 for i in range(m)]
        nodes = list(range(n + (2*m)))
        out_edges = collections.defaultdict(list)
        in_degree = collections.defaultdict(int)

        for item, (g, b) in enumerate(zip(group, beforeItems)):
            if g != -1:
                head, tail = heads[g], tails[g]
                out_edges[head].append(item)
                in_degree[item] += 1
                out_edges[item].append(tail)
                in_degree[tail] += 1
            
            for before in b:
                from_, to_ = group[before], group[item]
                same_group = from_ == to_
                out_ = before if same_group or from_ == -1 else tails[from_]
                to_ = item if same_group or to_ == -1 else heads[to_]
                out_edges[out_].append(to_)
                in_degree[to_] += 1

        starts = [node for node in nodes if not in_degree[node]]
        
        order = []
        for start in starts:
            order += self.topsort(collections.deque([start]), out_edges, in_degree)

        order = [node for node in order if node < n]
        return order if len(order) == n else []
