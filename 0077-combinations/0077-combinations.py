class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        comb = []

        def dfs(start):
            nonlocal comb

            if len(comb) == k:
                result.append(comb.copy())
                return
            
            if start > n:
                return

            comb.append(start)
            dfs(start + 1)
            comb.pop()
            dfs(start + 1)

        dfs(1)
        return result