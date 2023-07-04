class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        comb = []

        def dfs(start):
            nonlocal comb

            if len(comb) == k:
                result.append(comb.copy())
                return
                
            for i in range(start, n + 1):
                comb.append(i)
                dfs(i + 1)
                comb.pop()

        dfs(1)
        return result
        
        
        