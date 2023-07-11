class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def dfs(amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            
            if amount in dp:
                return dp[amount]
            
            min_cost = float("inf")
            for coin in coins:
                res = dfs(amount - coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)
            
            dp[amount] = min_cost if min_cost != float('inf') else -1
            return dp[amount]

        return dfs(amount)