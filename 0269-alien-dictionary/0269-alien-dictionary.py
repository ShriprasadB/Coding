class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:[] for w in words for c in w}
        indegree = collections.defaultdict(int)

        for i in range(len(words)-1):
            w1 , w2 = words[i], words[i + 1]
            
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    indegree[w2[j]] += 1
                    break
        
        queue = []
        for c in adj:
            if c not in indegree:
                queue.append(c)     
        
        ans = []
        while queue:
            m = len(queue)
            for i in range(m):
                node = queue.pop(0)
                ans.append(node)
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if indegree[nei] == 0:
                        queue.append(nei)
        
        return "".join(ans) if len(adj) == len(ans) else ""