class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        n = len(words)

        for i in range(1, n):
            w1, w2 = words[i - 1], words[i]
            min_len = min(len(w1), len(w2))

            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        answer = []
        visit = set()
        cycle = set()
        def dfs(c):
            if c in cycle:
                return False
            
            if c in visit:
                return True
            
            cycle.add(c)

            for nei in adj[c]:
                if not dfs(nei):
                    return False
            
            cycle.remove(c)
            visit.add(c)
            answer.append(c)
            return True

        for c in adj:
            if not dfs(c):
                return ""
        
        return "".join(answer)[::-1]