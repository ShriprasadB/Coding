class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:[] for w in words for c in w}
        n = len(words)
        indegree = collections.defaultdict(int)

        for i in range(1, n):
            w1, w2 = words[i - 1], words[i]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    indegree[w2[j]] += 1
                    break
            
        q = []
        for c in adj:
            if not indegree[c]:
                q.append(c)

        answer = []
        while q:
            node = q.pop(0)
            answer.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return "".join(answer) if len(answer) == len(adj) else ""
        